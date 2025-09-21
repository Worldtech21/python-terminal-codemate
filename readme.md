# Python Command Terminal

A sandboxed **Python-based command terminal** that mimics the behavior of a real system terminal.  
Built during the CodeMate Hackathon, this project demonstrates skills in **Python OOP, system-level programming, error handling, and testing**.

---

## 🚀 Features

- **File operations**
  - `ls` → list directory contents
  - `cd <dir>` → change directory
  - `pwd` → print working directory
  - `mkdir <dir>` → create directory
  - `rm <file/dir>` → remove files or directories

- **System monitoring** (via `psutil`)
  - `cpu` → CPU usage snapshot
  - `mem` → memory usage
  - `ps` → list top processes

- **Safety** → all operations are sandboxed to the project root  
- **Error handling** → friendly messages for invalid commands  
- **Extensible** → new commands can be added easily by subclassing `Command`  
- **Tested** → unit tests included (`pytest`)

---
## 📁Project Structure
```bash
python-terminal/
├── main.py # Entry point (REPL loop)
├── terminal.py # Terminal core (sandbox + dispatcher)
├── commands/ # Individual commands
│ ├── base.py
│ ├── ls.py, cd.py, pwd.py, mkdir.py, rm.py
│ ├── cpu.py, mem.py, ps.py
├── utils/ # Helpers
│ └── helpers.py
├── tests/ # Unit tests (pytest)
├── requirements.txt
└── README.md
```
---
## 🛠️ Setup

```bash
git clone https://github.com/Worldtech21/python-terminal--codemate.git
cd python-terminal--codemate
python -m venv .venv
.venv\Scripts\activate    # Windows
# or: source .venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
```
---
## 🏃🏼‍♂️Run
```bash
python main.py
```
---
## 💻 Example Session

```bash
> ls
> mkdir demo
> cd demo
> pwd
> cpu
> mem
> ps
> cd ..
> rm demo
> exit
```
---
## ✅ Testing
```bash
pytest -q
```
---
## 🎯 Skills Demonstrated

- **Python OOP**: Command design pattern for extensibility  
- **System-level programming**: File/directory operations, process inspection  
- **Safety & robustness**: Sandboxed environment, error handling  
- **Testing**: Unit tests with `pytest`  
- **Hackathon delivery**: Built under time constraints, end-to-end working demo  

## 📽️ Demo

- **Video**: [https://drive.google.com/file/d/1lyQb7r_eSTKacMFOuHgTXK4oFg86nPXr/view?usp=sharing]
- **Repository**: [https://github.com/Worldtech21/python-terminal-codemate]  
