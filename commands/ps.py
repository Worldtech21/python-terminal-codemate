from .base import Command
from typing import List
from terminal import Terminal

class PsCommand(Command):
    def execute(self, args: List[str], terminal: Terminal) -> None:
        try:
            procs = terminal.ps_list()
            print(f"{'PID':>6} {'NAME':<25} {'CPU%':>6} {'MEM%':>6}")
            for pid, name, cpu, mem in procs:
                print(f"{pid:>6} {str(name)[:25]:<25} {cpu if cpu is not None else 0:6} {mem if mem is not None else 0:6}")
        except Exception as e:
            print(f"ps: {e}")
