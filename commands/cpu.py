from .base import Command
from typing import List
from terminal import Terminal

class CpuCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        try:
            print(terminal.cpu_info())
        except Exception as e:
            print(f"cpu: {e}")
