"""
terminal.py - Terminal class: centralizes state and safe file operations.
Enforces sandbox: all paths are resolved under project_root.
"""

from pathlib import Path
import shutil
import psutil
from typing import Optional, List, Tuple

class Terminal:
    def __init__(self, project_root: Optional[Path] = None):
        # Default sandbox root = the folder containing this file's parent (project root)
        self.project_root = Path(project_root or Path.cwd()).resolve()
        self.current_dir = self.project_root
        # Basic command registry is imported lazily to avoid circular imports
        self._history: List[str] = []

    # --- path helpers ---
    def resolve(self, path: Optional[str]) -> Path:
        """
        Resolve a string path to an absolute Path within project_root.
        Raises ValueError if resolved path is outside the sandbox.
        """
        if not path or path.strip() == "":
            return self.current_dir
        p = (self.current_dir / path).expanduser().resolve()
        try:
            p.relative_to(self.project_root)
        except Exception:
            raise ValueError("Access denied: path is outside project root.")
        return p

    # --- file ops ---
    def list_dir(self, path: Optional[str] = None):
        p = self.resolve(path)
        if not p.exists():
            raise FileNotFoundError(f"No such file or directory: {p}")
        if p.is_file():
            return [p.name]
        return sorted([child.name for child in p.iterdir()])

    def change_dir(self, path: Optional[str] = None):
        p = self.resolve(path)
        if not p.exists() or not p.is_dir():
            raise NotADirectoryError(f"No such directory: {p}")
        self.current_dir = p

    def pwd(self) -> str:
        return str(self.current_dir.relative_to(self.project_root)) or "."

    def make_dir(self, path: str, parents: bool = False, exist_ok: bool = False):
        p = self.resolve(path)
        p.mkdir(parents=parents, exist_ok=exist_ok)

    def remove_path(self, path: str):
        p = self.resolve(path)
        if not p.exists():
            raise FileNotFoundError(f"No such file or directory: {p}")
        # If directory, remove recursively
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()

    # --- monitoring ---
    def cpu_info(self) -> str:
        # quick non-blocking snapshot
        per_cpu = psutil.cpu_percent(interval=0.1, percpu=True)
        avg = sum(per_cpu) / len(per_cpu) if per_cpu else 0.0
        return f"CPU average: {avg:.1f}% | per-cpu: {per_cpu}"

    def mem_info(self) -> str:
        vm = psutil.virtual_memory()
        return f"Memory: total={vm.total:,} bytes, used={vm.used:,} ({vm.percent}%)"

    def ps_list(self, limit: int = 20) -> List[Tuple[int, str, float, float]]:
        procs = []
        for p in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
            try:
                info = p.info
                procs.append((info.get("pid"), info.get("name"), info.get("cpu_percent"), info.get("memory_percent")))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        procs.sort(key=lambda x: (x[2] if x[2] is not None else 0.0), reverse=True)
        return procs[:limit]

    # --- REPL runner (keeps minimal parsing) ---
    def run(self):
        from commands import registry  # late import to pick up commands
        while True:
            prompt = f"{self.pwd()}> "
            try:
                raw = input(prompt).strip()
            except EOFError:
                print()  # newline on Ctrl-D
                break
            if not raw:
                continue
            self._history.append(raw)
            if raw in ("exit", "quit"):
                print("Exiting terminal...")
                break
            parts = raw.split()
            cmd_name, args = parts[0], parts[1:]
            cmd_cls = registry.get(cmd_name)
            if not cmd_cls:
                print(f"Unknown command: {cmd_name}")
                continue
            try:
                cmd = cmd_cls()
                cmd.execute(args, self)
            except Exception as e:
                print(f"Error: {e}")
