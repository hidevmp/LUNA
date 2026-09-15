import json
from pathlib import Path


MEMORY_FILE = Path(__file__).parent / "memory.json"


def load_memory():
    if not MEMORY_FILE.exists():
        return {
            "user": {},
            "facts": [],
            "preferences": []
        }

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii=False)


def remember_user(name, value):
    memory = load_memory()
    memory["user"][name] = value
    save_memory(memory)


def remember_fact(fact):
    memory = load_memory()

    if fact not in memory["facts"]:
        memory["facts"].append(fact)

    save_memory(memory)


def remember_preference(preference):
    memory = load_memory()

    if preference not in memory["preferences"]:
        memory["preferences"].append(preference)

    save_memory(memory)


def get_memory():
    return load_memory()