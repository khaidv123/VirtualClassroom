# core/persona.py
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Persona:
    agent_id: str
    name: str
    role: str = ""
    goal: str = ""
    backstory: str = ""
    tasks: str = "" 
    personality_traits: List[str] = field(default_factory=list)
    model: str = "gemini-2.0-flash" 
    tools: List[str] = field(default_factory=list)