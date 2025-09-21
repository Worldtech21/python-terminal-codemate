from .base import Command
from typing import List
from terminal import Terminal

class LsCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        path = args[0] if args else None
        try:
            items = terminal.list_dir(path)
            for item in items:
                print(item)
        except Exception as e:
            print(f"ls: {e}")
