Is there engine for writing text games in py ?  
If not write our own  
write some structure to it firsts  
then we will extend main body with components  

I'll organize this into a proper Python project structure with separate modules. Here's the complete project layout that I'll package for you:

```
text_game_engine/
├── game/
│   ├── __init__.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── movement.py
│   │   └── inventory.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── types.py
│   │   └── exceptions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── room.py
│   │   └── item.py
│   └── engine.py
├── cli.py
├── pyproject.toml
└── README.md
```

Here are the contents of each file:

### 1. `game/core/types.py`
```python
from enum import Enum, auto
from dataclasses import dataclass
from typing import Dict, List, Optional, Protocol, runtime_checkable

class GameState(Enum):
    RUNNING = auto()
    WON = auto()
    LOST = auto()
    QUIT = auto()

@dataclass
class GameResult:
    final_state: GameState
    score: int = 0
    message: str = ""

@runtime_checkable
class GameCommand(Protocol):
    name: str
    aliases: List[str]
    description: str
    
    def execute(self, context: 'GameContext') -> GameResult:
        ...

@dataclass
class GameContext:
    current_room: 'Room'
    inventory: Dict[str, 'Item']
    game_state: GameState = GameState.RUNNING
    variables: Dict[str, str] = None
```

### 2. `game/models/room.py`
```python
from dataclasses import dataclass
from typing import Dict, List
from ..core.types import GameCommand
from .item import Item

@dataclass
class Room:
    id: str
    name: str
    description: str
    exits: Dict[str, str]  # direction -> room_id
    items: List[Item]
    commands: List[GameCommand]
```

### 3. `game/models/item.py`
```python
from dataclasses import dataclass

@dataclass
class Item:
    id: str
    name: str
    description: str
    usable: bool = False
    takeable: bool = False
```

### 4. `game/commands/base.py`
```python
from ..core.types import GameCommand, GameResult, GameContext
from typing import List

class BaseCommand:
    def __init__(self, name: str, aliases: List[str], description: str):
        self.name = name
        self.aliases = aliases
        self.description = description
    
    def execute(self, context: GameContext) -> GameResult:
        raise NotImplementedError
```

### 5. `game/commands/movement.py`
```python
from .base import BaseCommand
from ..core.types import GameResult, GameContext

class MoveCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="move",
            aliases=["go", "walk", "run"],
            description="Move to another room"
        )
    
    def execute(self, context: GameContext) -> GameResult:
        # Implementation would handle movement between rooms
        return GameResult(context.game_state)
```

### 6. `game/commands/inventory.py`
```python
from .base import BaseCommand
from ..core.types import GameResult, GameContext

class InventoryCommand(BaseCommand):
    def __init__(self):
        super().__init__(
            name="inventory",
            aliases=["inv", "i"],
            description="Show your inventory"
        )
    
    def execute(self, context: GameContext) -> GameResult:
        if not context.inventory:
            print("Your inventory is empty")
        else:
            print("Inventory:")
            for item in context.inventory.values():
                print(f"- {item.name}: {item.description}")
        return GameResult(context.game_state)
```

### 7. `game/engine.py`
```python
from typing import Dict, List
from pathlib import Path
import json
from .models.room import Room
from .models.item import Item
from .core.types import GameContext, GameResult, GameState
from .commands.movement import MoveCommand
from .commands.inventory import InventoryCommand

class TextGameEngine:
    def __init__(self, game_data: Dict):
        self.rooms = self._load_rooms(game_data["rooms"])
        self.start_room_id = game_data["start_room"]
        self.commands = [
            MoveCommand(),
            InventoryCommand(),
        ]
    
    def _load_rooms(self, room_data: List[Dict]) -> Dict[str, Room]:
        return {
            room["id"]: Room(
                id=room["id"],
                name=room["name"],
                description=room["description"],
                exits=room.get("exits", {}),
                items=[Item(**item) for item in room.get("items", [])],
                commands=[]
            ) for room in room_data
        }
    
    def start(self) -> GameResult:
        context = GameContext(
            current_room=self.rooms[self.start_room_id],
            inventory={},
            variables={}
        )
        
        while context.game_state == GameState.RUNNING:
            self._display_room(context.current_room)
            command = self._get_player_input()
            result = self._execute_command(command, context)
            context.game_state = result.final_state
            
        return result
    
    def _display_room(self, room: Room):
        print(f"\n{room.name}\n")
        print(f"{room.description}\n")
        if room.items:
            print("You see: " + ", ".join(item.name for item in room.items))
        print("Exits: " + ", ".join(room.exits.keys()))
    
    def _get_player_input(self) -> str:
        return input("\nWhat would you like to do? ").strip().lower()
    
    def _execute_command(self, raw_input: str, context: GameContext) -> GameResult:
        for command in self.commands + context.current_room.commands:
            if (raw_input == command.name or 
                raw_input in command.aliases):
                return command.execute(context)
        
        print("I don't understand that command.")
        return GameResult(GameState.RUNNING)
```

### 8. `cli.py`
```python
from pathlib import Path
import typer
from game.engine import TextGameEngine

def load_game_data(game_file: Path) -> Dict:
    with open(game_file) as f:
        return json.load(f)

def main(
    game_file: Path = typer.Argument(..., help="JSON file containing game data"),
    debug: bool = typer.Option(False, help="Enable debug mode")
):
    """Run a text adventure game."""
    try:
        game_data = load_game_data(game_file)
        engine = TextGameEngine(game_data)
        result = engine.start()
        
        print(f"\nGame Over: {result.message}")
        print(f"Final Score: {result.score}")
    except Exception as e:
        if debug:
            raise
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    typer.run(main)
```

### 9. `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=42"]
build-backend = "setuptools.build_meta"

[project]
name = "text-game-engine"
version = "0.1.0"
description = "A modular text game engine for Python"
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
dependencies = [
    "typer >=0.9.0",
]
requires-python = ">=3.8"

[project.scripts]
text-game = "cli:main"
```

### 10. `README.md`
```markdown
# Python Text Game Engine

A modular, type-hinted text game engine for creating interactive fiction games.

## Installation

```bash
pip install .
```

## Usage

```bash
text-game path/to/game.json
```

## Creating Games

Create JSON files describing your game world. Example:

```json
{
  "start_room": "hallway",
  "rooms": [
    {
      "id": "hallway",
      "name": "Dark Hallway",
      "description": "A long, dark hallway with doors on either side.",
      "exits": {"north": "kitchen", "east": "library"},
      "items": [
        {"id": "torch", "name": "Torch", "description": "A flickering torch"}
      ]
    }
  ]
}
```

## Extending

Create new command classes in `game/commands/` to add functionality.
```

### Example Game JSON (`example_game.json`)
```json
{
  "start_room": "hallway",
  "rooms": [
    {
      "id": "hallway",
      "name": "Dark Hallway",
      "description": "A long, dark hallway with doors on either side.",
      "exits": {"north": "kitchen", "east": "library"},
      "items": [
        {"id": "torch", "name": "Torch", "description": "A flickering torch", "takeable": true}
      ]
    },
    {
      "id": "kitchen",
      "name": "Kitchen",
      "description": "A messy kitchen with strange smells.",
      "exits": {"south": "hallway"},
      "items": []
    },
    {
      "id": "library",
      "name": "Ancient Library",
      "description": "Dusty tomes line the walls.",
      "exits": {"west": "hallway"},
      "items": [
        {"id": "book", "name": "Strange Book", "description": "A book with glowing runes", "usable": true}
      ]
    }
  ]
}
```

Would you like me to make any adjustments to this structure or add specific features ?