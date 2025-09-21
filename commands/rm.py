from .base import Command
from typing import List
from terminal import Terminal

class RmCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        if not args:
            print("rm: missing operand")
            return
        for target in args:
            try:
                terminal.remove_path(target)
            except Exception as e:
                print(f"rm: {e}")
