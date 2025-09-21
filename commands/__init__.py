# command registry for terminal
from .ls import LsCommand
from .cd import CdCommand
from .pwd import PwdCommand
from .mkdir import MkdirCommand
from .rm import RmCommand
from .cpu import CpuCommand
from .mem import MemCommand
from .ps import PsCommand

registry = {
    "ls": LsCommand,
    "cd": CdCommand,
    "pwd": PwdCommand,
    "mkdir": MkdirCommand,
    "rm": RmCommand,
    "cpu": CpuCommand,
    "mem": MemCommand,
    "ps": PsCommand,
}
