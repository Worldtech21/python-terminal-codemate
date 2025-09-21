from .base import Command
from typing import List
from terminal import Terminal

class CdCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        target = args[0] if args else None
        try:
            terminal.change_dir(target)
        except Exception as e:
            print(f"cd: {e}")
