"""
Project: Python Command Terminal (Hackathon)
Goal: Create a Python backend that behaves like a real terminal. Mandatory commands: ls, cd, pwd, mkdir, rm. System monitoring commands: cpu, mem, ps. Must be sandboxed inside the project root. CLI REPL must handle errors gracefully. Use OOP: Command base class + command subclasses. Terminal class should centralize file operations and enforce sandbox. Use psutil for monitoring. Provide unit tests using pytest. Keep code simple, readable, well-documented, and easy for Copilot to expand. Files: main.py, terminal.py, commands/*, utils/helpers.py, tests/*, requirements.txt, README.md

Instructions for Copilot:
- When asked to generate a file, create that file with full content and imports.
- Use pathlib for file paths, psutil for monitoring, shutil/os where required.
- All operations must be limited to the project root (no destructive ops outside).
- Write unit tests that create temporary files (pytest tmp_path).
- Provide helpful error messages to the user.

"""

"""
main.py - entry point for Python Command Terminal
See COPILOT_SEED.md for overall project intent.

Run:
    python main.py
"""

from terminal import Terminal

def main():
    term = Terminal()
    try:
        term.run()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting terminal...")
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == "__main__":
    main()
