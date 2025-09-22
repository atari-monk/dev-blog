import os

structure = {
    "text_game_engine": {
        "game": {
            "commands": {
                "__init__.py": "",
                "base.py": "",
                "movement.py": "",
                "inventory.py": "",
            },
            "core": {
                "__init__.py": "",
                "types.py": "",
                "exceptions.py": "",
            },
            "models": {
                "__init__.py": "",
                "room.py": "",
                "item.py": "",
            },
            "__init__.py": "",
            "engine.py": "",
        },
        "cli.py": "",
        "pyproject.toml": "",
        "README.md": "",
    }
}


def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


if __name__ == "__main__":
    create_structure(".", structure)
