from .base import Command
from typing import List
from terminal import Terminal

class PwdCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        try:
            print(terminal.pwd())
        except Exception as e:
            print(f"pwd: {e}")
