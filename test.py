from utils.loaders import load_phases_from_yaml
from typing import Dict, Any, List, Tuple



def _load_and_process_phases(filepath: str) -> Dict[str, Dict]:
    """Loads phases and creates a map of task IDs for easy lookup."""
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


print(_load_and_process_phases("config/phases.yaml"))