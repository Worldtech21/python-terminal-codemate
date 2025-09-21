from .base import Command
from typing import List
from terminal import Terminal

class MkdirCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        if not args:
            print("mkdir: missing operand")
            return
        for dirname in args:
            try:
                terminal.make_dir(dirname, parents=True, exist_ok=False)
            except Exception as e:
                print(f"mkdir: {e}")
