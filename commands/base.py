from typing import List
from terminal import Terminal

class Command:
    """Base command class. Subclasses must implement execute()."""
    def execute(self, args: List[str], terminal: Terminal) -> None:
        raise NotImplementedError()
