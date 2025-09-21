from .base import Command
from typing import List
from terminal import Terminal

class MemCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        try:
            print(terminal.mem_info())
        except Exception as e:
            print(f"mem: {e}")
