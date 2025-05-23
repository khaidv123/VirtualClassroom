# core/conversation_phase_manager.py
import json
import traceback
from typing import Dict, Any, List, Tuple

from flask import Flask 
from core.conversation_history import ConversationHistory
from database.database import get_db
from services.llm_service import LLMService
from utils.loaders import load_phases_from_yaml
from core.prompts import *



class ConversationPhaseManager:
    def __init__(self, phase_config_path: str, problem_description: str, llm_service: LLMService, app_instance: Flask):
        self.phases = self._load_and_process_phases(phase_config_path)
        if not self.phases:
            raise ValueError("Failed to load phase configurations.")
        self.problem = problem_description
        self.llm_service = llm_service
        self.app = app_instance
        print(f"--- PHASE_MGR: Initialized.")

    def _load_and_process_phases(self, filepath: str) -> Dict[str, Dict]:
        phases_cfg = load_phases_from_yaml(filepath)
        if not phases_cfg: return {}
        for phase_id, phase_data in phases_cfg.items():
            if 'tasks' in phase_data and isinstance(phase_data['tasks'], list):
                task_map = {}
                processed_tasks = []
                for task_idx, task_item in enumerate(phase_data['tasks']):
                    if isinstance(task_item, dict) and 'id' in task_item and 'description' in task_item:
                        task_map[task_item['id']] = task_item['description']
                        processed_tasks.append(task_item)
                    elif isinstance(task_item, str):
                        print(f"!!! WARN [PhaseManager]: Task in phase {phase_id} is a string, converting. Please update YAML. Task: {task_item}")
                        new_task_id = f"{phase_id}.{task_idx + 1}_auto"
                        task_map[new_task_id] = task_item
                        processed_tasks.append({'id': new_task_id, 'description': task_item})
                    else:
                        print(f"!!! WARN [PhaseManager]: Invalid task format in phase {phase_id}: {task_item}")
                phase_data['_task_map'] = task_map
                phase_data['tasks'] = processed_tasks
        return phases_cfg

    def _get_session_state(self, session_id: str) -> Tuple[str, Dict[str, List[str]]]:
        db = get_db()
        state_row = db.execute(
            "SELECT current_phase_id, metadata FROM sessions WHERE session_id = ?", (session_id,)
        ).fetchone()

        if not state_row:
            print(f"!!! WARN [PhaseManager - {session_id}]: Session not found in DB. Defaulting state.")
            return "1", {}

        last_known_phase_id = state_row['current_phase_id'] or "1"
        
        
        raw_db_metadata = state_row['metadata']
        metadata = {}
        if raw_db_metadata:
            if isinstance(raw_db_metadata, dict):
                metadata = raw_db_metadata
            elif isinstance(raw_db_metadata, (str, bytes, bytearray)):
                try:
                    metadata = json.loads(raw_db_metadata)
                except json.JSONDecodeError:
                    print(f"!!! WARN [PhaseManager - {session_id}]: Could not decode metadata JSON: '{raw_db_metadata}'. Defaulting metadata.")
            else:
                print(f"!!! WARN [PhaseManager - {session_id}]: Metadata from DB is of unexpected type: {type(raw_db_metadata)}. Defaulting metadata.")
        
        completed_tasks_map = metadata.get("completed_tasks", {})
        if not isinstance(completed_tasks_map, dict):
            print(f"!!! WARN [PhaseManager - {session_id}]: 'completed_tasks' in metadata is not a dict: {completed_tasks_map}. Defaulting to empty dict.")
            completed_tasks_map = {}
        
        # Ensure all values in completed_tasks_map are lists
        for phase_key in list(completed_tasks_map.keys()): 
            if not isinstance(completed_tasks_map[phase_key], list):
                print(f"!!! WARN [PhaseManager - {session_id}]: Tasks for phase {phase_key} in DB metadata was not a list: {completed_tasks_map[phase_key]}. Correcting to empty list.")
                completed_tasks_map[phase_key] = []


        return last_known_phase_id, completed_tasks_map

    def _update_session_state(self, session_id: str, new_phase_id_to_set_in_db: str, completed_tasks_map_to_save: Dict[str, List[str]]):
        db = get_db()
        current_metadata_row = db.execute("SELECT metadata FROM sessions WHERE session_id = ?", (session_id,)).fetchone()
        
        existing_metadata = {}
        if current_metadata_row and current_metadata_row['metadata']:
            raw_current_db_metadata = current_metadata_row['metadata']
            if isinstance(raw_current_db_metadata, dict):
                existing_metadata = raw_current_db_metadata
            elif isinstance(raw_current_db_metadata, (str, bytes, bytearray)):
                try:
                    existing_metadata = json.loads(raw_current_db_metadata)
                except json.JSONDecodeError:
                    print(f"!!! WARN [PhaseManager - {session_id}]: Could not decode existing metadata JSON during update: '{raw_current_db_metadata}'. Starting fresh metadata.")
            else:
                print(f"!!! WARN [PhaseManager - {session_id}]: Existing metadata from DB is of unexpected type during update: {type(raw_current_db_metadata)}. Starting fresh metadata.")

        
        if "completed_tasks" not in existing_metadata or not isinstance(existing_metadata["completed_tasks"], dict):
             existing_metadata["completed_tasks"] = {}
        
        # Update the completed_tasks part of existing_metadata with new data
        # Ensure values in completed_tasks_map_to_save are lists and deduplicated
        for phase_id, tasks in completed_tasks_map_to_save.items():
            if isinstance(tasks, list):
                existing_metadata["completed_tasks"][phase_id] = list(set(str(t) for t in tasks)) 
            else:
                print(f"!!! WARN [PhaseManager - {session_id}]: Tasks for phase {phase_id} in completed_tasks_map_to_save is not a list: {tasks}. Retaining existing or initializing as empty list.")
                if phase_id not in existing_metadata["completed_tasks"] or not isinstance(existing_metadata["completed_tasks"][phase_id], list):
                    existing_metadata["completed_tasks"][phase_id] = []


        try:
            db.execute(
                "UPDATE sessions SET current_phase_id = ?, metadata = ? WHERE session_id = ?",
                (new_phase_id_to_set_in_db, json.dumps(existing_metadata), session_id)
            )
            db.commit()
            print(f"--- PHASE_MGR [{session_id}]: Updated session state in DB - Phase: {new_phase_id_to_set_in_db}, Metadata tasks: {existing_metadata.get('completed_tasks')}")
        except Exception as e:
            print(f"!!! ERROR [PhaseManager - {session_id}]: Failed to update session state in DB: {e}")
            traceback.print_exc()
            db.rollback()

    def _format_task_status_for_prompt(self, phase_id_for_status: str, completed_tasks_map: Dict[str, List[str]]) -> str:
        phase_def_for_status = self.phases.get(phase_id_for_status)
        if not phase_def_for_status or 'tasks' not in phase_def_for_status:
            return "Không có nhiệm vụ nào được định nghĩa cho giai đoạn này."

        tasks_in_phase = phase_def_for_status.get('tasks', [])
        completed_ids_for_this_phase = []
        if isinstance(completed_tasks_map, dict):
            completed_ids_for_this_phase = completed_tasks_map.get(phase_id_for_status, [])
        else:
            print(f"!!! WARN [PhaseManager]: _format_task_status_for_prompt received non-dict completed_tasks_map for phase {phase_id_for_status}. Defaulting to no tasks completed.")

        status_lines = []
        next_task_found = False
        if not tasks_in_phase:
            return "Giai đoạn này không có nhiệm vụ cụ thể nào được liệt kê."
            
        for task_dict in tasks_in_phase:
            task_id = task_dict.get('id')
            task_desc = task_dict.get('description')
            if task_id is None or task_desc is None: continue 

            is_done = str(task_id) in [str(cid) for cid in completed_ids_for_this_phase] 
            marker = "[X]" if is_done else "[ ]"
            next_marker = ""
            if not is_done and not next_task_found:
                next_marker = " <-- Nhiệm vụ tiếp theo cần tập trung"
                next_task_found = True
            status_lines.append(f"- {marker} ({task_id}) {task_desc}{next_marker}")

        if not status_lines: return "Không có nhiệm vụ nào cho giai đoạn này."
        return "\n".join(status_lines)

    def mark_task_complete(self, session_id: str, task_id_to_complete: str):
        current_phase_id_from_db, completed_tasks_map = self._get_session_state(session_id)
        
        print(f"Debug (mark_task_complete): last known phase id from DB is '{current_phase_id_from_db}' for session '{session_id}' when attempting to mark task '{task_id_to_complete}'.")


        phase_to_update_tasks_for = current_phase_id_from_db

        if phase_to_update_tasks_for not in self.phases:
            print(f"!!! WARN [PhaseManager - {session_id}]: Phase '{phase_to_update_tasks_for}' (for task '{task_id_to_complete}') not defined in phases config. Skipping task mark.")
            return

        if not isinstance(completed_tasks_map, dict):
            print(f"!!! WARN [PhaseManager - {session_id}]: completed_tasks_map is not a dict in mark_task_complete. Initializing.")
            completed_tasks_map = {}

        if phase_to_update_tasks_for not in completed_tasks_map:
            completed_tasks_map[phase_to_update_tasks_for] = []
        elif not isinstance(completed_tasks_map[phase_to_update_tasks_for], list):
            print(f"!!! WARN [PhaseManager - {session_id}]: Tasks for phase '{phase_to_update_tasks_for}' was not a list. Resetting for task '{task_id_to_complete}'.")
            completed_tasks_map[phase_to_update_tasks_for] = []

        defined_tasks_for_phase_map = self.phases[phase_to_update_tasks_for].get('_task_map', {})
        if str(task_id_to_complete) not in defined_tasks_for_phase_map: 
            print(f"!!! WARN [PhaseManager - {session_id}]: Task ID '{task_id_to_complete}' is not a defined task for phase '{phase_to_update_tasks_for}'. Defined tasks: {list(defined_tasks_for_phase_map.keys())}. Skipping task mark.")
            return

        str_task_id_to_complete = str(task_id_to_complete)
        if str_task_id_to_complete not in [str(t) for t in completed_tasks_map[phase_to_update_tasks_for]]: 
            completed_tasks_map[phase_to_update_tasks_for].append(str_task_id_to_complete) 
            print(f"--- PHASE_MGR [{session_id}]: Marking task '{str_task_id_to_complete}' as complete for phase '{phase_to_update_tasks_for}'.")
            self._update_session_state(session_id, current_phase_id_from_db, completed_tasks_map)
        else:
            print(f"--- PHASE_MGR [{session_id}]: Task '{str_task_id_to_complete}' already marked complete for phase '{phase_to_update_tasks_for}'.")

    def get_phase_context(self, session_id: str, conversation_history: ConversationHistory) -> Dict[str, Any]:
        with self.app.app_context():
            last_known_phase_id, completed_tasks_map_before_llm = self._get_session_state(session_id)
            print(f"Debug (get_phase_context start): last known phase id from DB is '{last_known_phase_id}' for session '{session_id}'.")

            history_log = conversation_history.get_history(session_id=session_id)

            current_phase_def_for_llm_prompt = self.phases.get(last_known_phase_id)
            if not current_phase_def_for_llm_prompt:
                print(f"!!! ERROR [PhaseManager - {session_id}]: Config for last known phase '{last_known_phase_id}' not found. Defaulting to '1'.")
                last_known_phase_id = "1"
                current_phase_def_for_llm_prompt = self.phases.get("1", {})
                if not current_phase_def_for_llm_prompt:
                    return {"id": "?", "name": "Config Error", "description": "Phase configuration missing.", "tasks_for_display": [], "goals": [], "task_status_prompt": "Lỗi cấu hình giai đoạn.", "completed_tasks_map": {}}

            current_stage_desc_prompt = f"Giai đoạn hiện tại (ID: {last_known_phase_id}): {current_phase_def_for_llm_prompt.get('name', '')}\n"
            current_stage_desc_prompt += f"Mô tả giai đoạn: {current_phase_def_for_llm_prompt.get('description', '')}\n"
            current_stage_desc_prompt += "Danh sách nhiệm vụ của giai đoạn này (ID, trạng thái `[X] - Hoàn thành` / `[ ] - Chưa Hoàn thành`, và mô tả):\n"
            
            tasks_for_llm_prompt = current_phase_def_for_llm_prompt.get('tasks', [])
            completed_ids_for_this_phase_in_prompt = []
            if isinstance(completed_tasks_map_before_llm, dict):
                completed_ids_for_this_phase_in_prompt = [str(tid) for tid in completed_tasks_map_before_llm.get(last_known_phase_id, [])]


            if tasks_for_llm_prompt:
                for t_dict in tasks_for_llm_prompt:
                    task_id = t_dict.get('id')
                    task_desc = t_dict.get('description')
                    if task_id and task_desc:
                        marker = "[X]" if str(task_id) in completed_ids_for_this_phase_in_prompt else "[ ]"
                        current_stage_desc_prompt += f"- {marker} ({task_id}) {task_desc}\n"
                    else:
                        current_stage_desc_prompt += f"- (Nhiệm vụ không hợp lệ: {t_dict})\n"
            else:
                current_stage_desc_prompt += "- (Không có nhiệm vụ cụ thể nào được liệt kê cho giai đoạn này)\n"
            
            current_stage_desc_prompt += "Mục tiêu của giai đoạn:\n"
            goals_list = current_phase_def_for_llm_prompt.get('goals', [])
            if goals_list:
                current_stage_desc_prompt += "\n".join([f"- {g}" for g in goals_list])
            else:
                current_stage_desc_prompt += "(Không có mục tiêu cụ thể cho giai đoạn này)"

            prompt = STAGE_MANAGER_PROMPT.format(
                problem=self.problem,
                current_stage_description=current_stage_desc_prompt.strip(),
                history=self._format_history_for_prompt(history_log)
            )

            print(f"--- PHASE_MGR [{session_id}]: Requesting phase signal & task completion from LLM (based on stage {last_known_phase_id})...")
            
            llm_determined_signal_text = "Tiếp tục"
            completed_task_ids_from_llm = []
            raw_response_for_log = "N/A"

            try:
                raw_response = self.llm_service.generate(prompt)
                raw_response_for_log = raw_response
                print(f"--- PHASE_MGR [{session_id}]: Raw LLM Signal Response: {raw_response}")
                
                json_match = None
                try:
                    # More robust JSON extraction
                    start_index = raw_response.find('{')
                    end_index = raw_response.rfind('}') + 1
                    if start_index != -1 and end_index != 0 and end_index > start_index:
                        json_str_candidate = raw_response[start_index:end_index]
                        parsed_output = json.loads(json_str_candidate)
                        json_match = True
                    else: 
                        clean_response = raw_response.strip().replace("```json", "").replace("```", "").replace("{{", "{").replace("}}", "}")
                        parsed_output = json.loads(clean_response)

                except json.JSONDecodeError as je:
                    print(f"!!! WARN [PhaseManager - {session_id}]: Failed to parse LLM JSON response: {je}. Raw: {raw_response_for_log}")
                    

                if json_match or 'parsed_output' in locals(): 
                    signal_data = parsed_output.get("signal")
                    raw_completed_task_ids_from_llm = parsed_output.get("completed_task_ids", [])
                    
                    if isinstance(raw_completed_task_ids_from_llm, list):
                        completed_task_ids_from_llm = [str(tid).strip() for tid in raw_completed_task_ids_from_llm if isinstance(tid, (str, int, float)) and str(tid).strip()]
                    else:
                        print(f"!!! WARN [PhaseManager - {session_id}]: 'completed_task_ids' from LLM is not a list: {raw_completed_task_ids_from_llm}. Ignoring.")
                    
                    if isinstance(signal_data, list) and len(signal_data) == 2:
                        _, signal_text_from_llm = map(str, signal_data)
                        llm_determined_signal_text = signal_text_from_llm.strip()
                    else:
                        print(f"!!! WARN [PhaseManager - {session_id}]: Invalid 'signal' format from LLM: {signal_data}. Defaulting signal to 'Tiếp tục'.")
                    
                    print(f"--- PHASE_MGR [{session_id}]: LLM Signal: '{llm_determined_signal_text}'. Tasks suggested by LLM: {completed_task_ids_from_llm}.")
            
            except Exception as e: 
                print(f"!!! ERROR [PhaseManager - {session_id}]: General error during LLM interaction or parsing: {e}. Raw: {raw_response_for_log}")
                traceback.print_exc()


            if completed_task_ids_from_llm:
                defined_task_ids_for_prompted_phase = current_phase_def_for_llm_prompt.get('_task_map', {}).keys()
                
                for task_id_from_llm in completed_task_ids_from_llm:
                    str_task_id_from_llm = str(task_id_from_llm)
                    if str_task_id_from_llm in defined_task_ids_for_prompted_phase:
                        self.mark_task_complete(session_id, str_task_id_from_llm)
                    else:
                        print(f"!!! WARN [PhaseManager - {session_id}]: LLM suggested task '{str_task_id_from_llm}' as complete, "
                              f"but it does not belong to the phase '{last_known_phase_id}' "
                              f"(defined tasks for this phase: {list(defined_task_ids_for_prompted_phase)}) "
                              f"that the LLM was prompted with. Discarding this task suggestion.")
            
            current_phase_id_for_logic, completed_tasks_map_after_llm_updates = self._get_session_state(session_id)
            
            final_phase_id_for_context = current_phase_id_for_logic
            final_completed_tasks_map_for_context = json.loads(json.dumps(completed_tasks_map_after_llm_updates)) # Deep copy

            if llm_determined_signal_text == "Chuyển stage mới" or signal_data[1] == "4":
                tasks_in_current_phase_logic_def = self.phases.get(current_phase_id_for_logic, {}).get('tasks', [])
                defined_task_ids_current_phase_logic = {str(t['id']) for t in tasks_in_current_phase_logic_def if isinstance(t, dict) and 'id' in t}
                
                completed_ids_current_phase_logic_list = final_completed_tasks_map_for_context.get(current_phase_id_for_logic, [])
                completed_ids_current_phase_logic_set = {str(tid) for tid in completed_ids_current_phase_logic_list}

                all_tasks_of_current_phase_completed = defined_task_ids_current_phase_logic.issubset(completed_ids_current_phase_logic_set)

                if not all_tasks_of_current_phase_completed and defined_task_ids_current_phase_logic:
                    print(f"--- PHASE_MGR [{session_id}]: LLM signaled 'Chuyển stage mới', but not all tasks for phase '{current_phase_id_for_logic}' are complete. "
                          f"Required: {defined_task_ids_current_phase_logic}, Completed: {completed_ids_current_phase_logic_set}. Staying in current phase.")
                    self._update_session_state(session_id, current_phase_id_for_logic, final_completed_tasks_map_for_context)
                else:
                    try:
                        next_phase_int = int(current_phase_id_for_logic) + 1
                        next_phase_id_str = str(next_phase_int)
                        if next_phase_id_str in self.phases:
                            final_phase_id_for_context = next_phase_id_str
                            print(f"--- PHASE_MGR [{session_id}]: Transitioning from stage '{current_phase_id_for_logic}' to '{final_phase_id_for_context}'.")
                            
                            if final_phase_id_for_context not in final_completed_tasks_map_for_context:
                                final_completed_tasks_map_for_context[final_phase_id_for_context] = []
                            elif not isinstance(final_completed_tasks_map_for_context.get(final_phase_id_for_context), list):
                                print(f"--- PHASE_MGR [{session_id}]: Resetting tasks for new phase {final_phase_id_for_context} as it was not a list.")
                                final_completed_tasks_map_for_context[final_phase_id_for_context] = []
                            
                            self._update_session_state(session_id, final_phase_id_for_context, final_completed_tasks_map_for_context)
                        else:
                            print(f"--- PHASE_MGR [{session_id}]: LLM signaled transition, but next stage '{next_phase_id_str}' not found. Staying in '{current_phase_id_for_logic}'.")
                            self._update_session_state(session_id, current_phase_id_for_logic, final_completed_tasks_map_for_context)
                    except ValueError:
                        print(f"!!! ERROR [PhaseManager - {session_id}]: Cannot increment phase ID '{current_phase_id_for_logic}'. Staying in current phase.")
                        self._update_session_state(session_id, current_phase_id_for_logic, final_completed_tasks_map_for_context)
            else:
                self._update_session_state(session_id, current_phase_id_for_logic, final_completed_tasks_map_for_context)

            task_status_prompt_for_output = self._format_task_status_for_prompt(final_phase_id_for_context, final_completed_tasks_map_for_context)
            final_phase_data_def = self.phases.get(final_phase_id_for_context, {})

            tasks_for_ui_display = []
            defined_tasks_in_final_phase = final_phase_data_def.get('tasks', [])
            
            
            print(f"--- PHASE_MGR [{session_id}]: Preparing tasks for UI. Final Phase ID: {final_phase_id_for_context}")
            print(f"--- PHASE_MGR [{session_id}]: Final phase data definition from config: {final_phase_data_def.get('name', 'N/A')}, Tasks: {defined_tasks_in_final_phase}")
            # print(f"--- PHASE_MGR [{session_id}]: Raw defined tasks for this phase from config: {defined_tasks_in_final_phase}") # Original log line

            completed_task_ids_in_final_phase_list = []
            if isinstance(final_completed_tasks_map_for_context, dict):
                 completed_task_ids_in_final_phase_list = [str(tid) for tid in final_completed_tasks_map_for_context.get(final_phase_id_for_context, [])]
            
            for task_dict in defined_tasks_in_final_phase:
                if isinstance(task_dict, dict) and 'id' in task_dict and 'description' in task_dict:
                    tasks_for_ui_display.append({
                        "id": str(task_dict['id']),
                        "description": task_dict['description'],
                        "completed": str(task_dict['id']) in completed_task_ids_in_final_phase_list
                    })
                else:
                    print(f"!!! WARN [PhaseManager - {session_id}]: Corrupt task item in final_phase_data_def for phase {final_phase_id_for_context}: {task_dict}")

            return {
                "id": final_phase_id_for_context,
                "name": final_phase_data_def.get('name', f'Unknown Phase {final_phase_id_for_context}'),
                "description": final_phase_data_def.get('description', ''),
                "tasks_for_display": tasks_for_ui_display,
                "goals": final_phase_data_def.get('goals', []),
                "task_status_prompt": task_status_prompt_for_output,
                "completed_tasks_map": final_completed_tasks_map_for_context
            }

    def _format_history_for_prompt(self, history: List[Dict], count=100) -> str:
        recent_history = history[-count:]
        lines = []
        for i, event in enumerate(recent_history):
            text = event.get('content', {}).get('text', '(Non-message event)')
            source_display = event.get('content', {}).get('sender_name', event.get('source', 'Unknown'))
            lines.append(f"CON#{i+1} {source_display}: {text}")
        return "\n".join(lines) if lines else "Chưa có hội thoại."

    def _update_session_phase_in_db(self, session_id: str, new_phase_id: str):
        try:
            db = get_db()
            db.execute(
                "UPDATE sessions SET current_phase_id = ? WHERE session_id = ?",
                (new_phase_id, session_id)
            )
            db.commit()
            print(f"--- PHASE_MGR [{session_id}]: Updated session phase (only phase_id column) in DB to '{new_phase_id}'.")
        except Exception as e:
            print(f"!!! ERROR [PhaseManager - {session_id}]: Failed to update session phase (only phase_id column) in DB: {e}")
            db.rollback()

    def _determine_phase_state(self, session_id: str, conversation_history: ConversationHistory) -> Dict[str, Any]:
        with self.app.app_context():
            try:
                db = get_db()
                session_data = db.execute(
                    "SELECT current_phase_id FROM sessions WHERE session_id = ?", (session_id,)
                ).fetchone()

                last_known_phase_id_from_db = "1"
                if session_data and session_data['current_phase_id']:
                    last_known_phase_id_from_db = session_data['current_phase_id']
                elif session_data:
                     print(f"!!! WARN [PhaseManager (_determine_phase_state) - {session_id}]: current_phase_id is null in DB. Defaulting to '1'.")
                     self._update_session_phase_in_db(session_id, last_known_phase_id_from_db)
                else:
                     print(f"!!! ERROR [PhaseManager (_determine_phase_state) - {session_id}]: Session data not found in DB. Defaulting phase to '1'.")

                print(f"--- PHASE_MGR (_determine_phase_state) [{session_id}]: Last known phase from DB: '{last_known_phase_id_from_db}'.")

                history_log = conversation_history.get_history(session_id=session_id)
                current_phase_def_for_prompt = self.phases.get(last_known_phase_id_from_db)

                if not history_log:
                    print(f"--- PHASE_MGR (_determine_phase_state) [{session_id}]: No history yet, using phase '{last_known_phase_id_from_db}'.")
                    current_phase_data_to_return = self.phases.get(last_known_phase_id_from_db, self.phases.get("1", {}))
                    return {"id": last_known_phase_id_from_db, "last_signal": "Bắt đầu", "name": current_phase_data_to_return.get('name', f'Unknown Phase {last_known_phase_id_from_db}'), **current_phase_data_to_return}

                if not current_phase_def_for_prompt:
                    print(f"!!! ERROR [PhaseManager (_determine_phase_state) - {session_id}]: Config for phase ID '{last_known_phase_id_from_db}' not found. Defaulting check to '1'.")
                    last_known_phase_id_from_db = "1"
                    current_phase_def_for_prompt = self.phases.get("1", {})
                    if not current_phase_def_for_prompt:
                        return {"id": "?", "last_signal": "Error", "name": "Config Error"}

                current_stage_desc_prompt_simple = f"Stage {last_known_phase_id_from_db}: {current_phase_def_for_prompt.get('name', 'Không rõ')}\n"
                current_stage_desc_prompt_simple += f"Description: {current_phase_def_for_prompt.get('description', 'Không có mô tả')}\n"
                tasks_list = current_phase_def_for_prompt.get('tasks', [])
                current_stage_desc_prompt_simple += "Tasks:\n" + ("\n".join([f"- ({t.get('id')}) {t.get('description')}" for t in tasks_list if isinstance(t, dict)]) + "\n" if tasks_list else "(Không có nhiệm vụ cụ thể cho giai đoạn này)\n")
                goals_list = current_phase_def_for_prompt.get('goals', [])
                current_stage_desc_prompt_simple += "Goals:\n" + ("\n".join([f"- {g}" for g in goals_list]) + "\n" if goals_list else "(Không có mục tiêu cụ thể cho giai đoạn này)\n")

                prompt = STAGE_MANAGER_PROMPT.format(
                    problem=self.problem,
                    current_stage_description=current_stage_desc_prompt_simple.strip(),
                    history=self._format_history_for_prompt(history_log)
                )

                print(f"--- PHASE_MGR (_determine_phase_state) [{session_id}]: Requesting phase update from LLM (based on stage {last_known_phase_id_from_db})...")

                final_determined_phase_id = last_known_phase_id_from_db
                determined_signal_text = "Tiếp tục"
                
                raw_response = self.llm_service.generate(prompt)
                print(f"--- PHASE_MGR (_determine_phase_state) [{session_id}]: Raw LLM Response: {raw_response}")

                try:
                    # Attempt to find JSON block
                    json_str_candidate = raw_response 
                    start_index = raw_response.find('{')
                    end_index = raw_response.rfind('}') + 1
                    if start_index != -1 and end_index != 0 and end_index > start_index:
                        json_str_candidate = raw_response[start_index:end_index]
                    
                    parsed_output = json.loads(json_str_candidate)
                    signal_data = parsed_output.get("signal")

                    if isinstance(signal_data, list) and len(signal_data) == 2:
                        signal_code, signal_text_from_llm = map(str, signal_data)
                        determined_signal_text = signal_text_from_llm.strip()

                        if determined_signal_text == "Chuyển stage mới" or signal_code == "4":
                            try:
                                next_phase_int = int(last_known_phase_id_from_db) + 1
                                next_phase_id_str = str(next_phase_int)
                                if next_phase_id_str in self.phases:
                                    final_determined_phase_id = next_phase_id_str
                                    determined_signal_text = "Bắt đầu"
                                else:
                                    determined_signal_text = "Đưa ra tín hiệu kết thúc"
                            except ValueError:
                                print(f"!!! ERROR [PhaseManager (_determine_phase_state) - {session_id}]: Cannot increment phase ID '{last_known_phase_id_from_db}'.")
                                determined_signal_text = "Error"
                except Exception as e:
                     print(f"!!! ERROR [PhaseManager (_determine_phase_state) - {session_id}]: Error processing LLM response: {e}")
                     if isinstance(e, json.JSONDecodeError): print(f"Raw response was: {raw_response}")
                     traceback.print_exc()

                if final_determined_phase_id != last_known_phase_id_from_db:
                    self._update_session_phase_in_db(session_id, final_determined_phase_id)

                final_phase_data_to_return = self.phases.get(final_determined_phase_id, {})
                return {
                    "id": final_determined_phase_id,
                    "last_signal": determined_signal_text,
                    "name": final_phase_data_to_return.get('name', f'Unknown Phase {final_determined_phase_id}'),
                    "description": final_phase_data_to_return.get('description', ''),
                    "tasks": final_phase_data_to_return.get('tasks', []),
                    "goals": final_phase_data_to_return.get('goals', []),
                }
            except Exception as e:
                 print(f"!!! ERROR [PhaseManager (_determine_phase_state) - {session_id}]: Failed during phase determination: {e}")
                 traceback.print_exc()
                 return {"id": "?", "last_signal": "Error", "name": "Processing Error"}

    def get_current_phase(self, session_id: str, conversation_history: ConversationHistory = None) -> Dict[str, Any]:
        with self.app.app_context():
            current_phase_id_from_db, completed_tasks_map_from_db = self._get_session_state(session_id)
            phase_data_from_config = self.phases.get(current_phase_id_from_db, {})
            
            tasks_for_ui_display = []
            defined_tasks = phase_data_from_config.get('tasks', [])
            
            completed_ids_for_current_phase = []
            if isinstance(completed_tasks_map_from_db, dict):
                completed_ids_for_current_phase = [str(tid) for tid in completed_tasks_map_from_db.get(current_phase_id_from_db, [])]

            for task_dict in defined_tasks:
                if isinstance(task_dict, dict) and 'id' in task_dict and 'description' in task_dict:
                    task_id_str = str(task_dict['id'])
                    tasks_for_ui_display.append({
                        "id": task_id_str,
                        "description": task_dict['description'],
                        "completed": task_id_str in completed_ids_for_current_phase
                    })

            return {
                "id": current_phase_id_from_db,
                "name": phase_data_from_config.get('name', f'Unknown Phase {current_phase_id_from_db}'),
                "description": phase_data_from_config.get('description', ''),
                "tasks_for_display": tasks_for_ui_display,
                "goals": phase_data_from_config.get('goals', []),
                "completed_tasks_map": completed_tasks_map_from_db
            }