# utils/loaders.py
import traceback
import yaml
import uuid
from typing import Dict, List, Optional
from core.persona import Persona

def load_personas_from_yaml(filepath: str) -> Dict[str, Persona]:
    """Loads agent personas from a YAML file."""
    personas = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            agents_cfg = yaml.safe_load(f)

        if not isinstance(agents_cfg, dict):
             print(f"!!! ERROR [Loader]: Invalid YAML format in {filepath}. Expected a dictionary.")
             return {}

        for agent_name, props in agents_cfg.items():
            if not isinstance(props, dict):
                 print(f"!!! WARN [Loader]: Skipping invalid entry for '{agent_name}' in {filepath}.")
                 continue

            agent_id = str(uuid.uuid4())

            persona = Persona(
                agent_id=agent_id,
                name=agent_name,
                role=props.get('role', ''),
                goal=props.get('goal', ''),
                backstory=props.get('backstory', ''),
               
                tasks=props.get('tasks', ''), 
                personality_traits=props.get('personality_traits', []),
                model=props.get('model', 'gemini-2.0-flash'),
                tools=props.get('tools', [])
            )
            personas[agent_id] = persona
            print(f"--- LOADER: Loaded persona for {agent_name} with ID {agent_id}")

    except FileNotFoundError:
        print(f"!!! ERROR [Loader]: Persona configuration file not found: {filepath}")
    except yaml.YAMLError as e:
        print(f"!!! ERROR [Loader]: Error parsing YAML file {filepath}: {e}")
    except Exception as e:
        print(f"!!! ERROR [Loader]: Unexpected error loading personas from {filepath}: {e}")

    return personas


def load_phases_from_yaml(filepath: str) -> Dict[str, Dict]:
    """Loads conversation phase definitions from a YAML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            phases_cfg = yaml.safe_load(f)
        if not isinstance(phases_cfg, dict):
             print(f"!!! ERROR [Loader]: Invalid YAML format in {filepath}. Expected a dictionary for phases.")
             return {}
        # TODO: Add validation for phase structure if needed
        print(f"--- LOADER: Loaded {len(phases_cfg)} phases from {filepath}")
        return phases_cfg
    except FileNotFoundError:
        print(f"!!! WARN [Loader]: Phase configuration file not found: {filepath}. Using defaults.")
        return {} 
    except yaml.YAMLError as e:
        print(f"!!! ERROR [Loader]: Error parsing YAML file {filepath}: {e}")
        return {}
    except Exception as e:
        print(f"!!! ERROR [Loader]: Unexpected error loading phases from {filepath}: {e}")
        return {}
    
def load_problem_context(filepath: str) -> Optional[Dict[str, str]]:
    """Loads problem and solution descriptions from a YAML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            context_cfg = yaml.safe_load(f)
        if not isinstance(context_cfg, dict) or 'problem' not in context_cfg:
             print(f"!!! ERROR [Loader]: Invalid format or missing 'problem' key in {filepath}.")
             return None
        print(f"--- LOADER: Loaded problem context from {filepath}")
        
        return {
            'problem': context_cfg.get('problem', ''),
            'solution': context_cfg.get('solution', '') 
        }
    except FileNotFoundError:
        print(f"!!! ERROR [Loader]: Problem context file not found: {filepath}")
        return None
    except yaml.YAMLError as e:
        print(f"!!! ERROR [Loader]: Error parsing YAML file {filepath}: {e}")
        return None
    except Exception as e:
        print(f"!!! ERROR [Loader]: Unexpected error loading problem context from {filepath}: {e}")
        traceback.print_exc() 
        return None