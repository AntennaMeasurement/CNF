# Antenna Measurement CNF

A Python package for antenna measurement CNF utilities.

## Installation

```bash
pip install antenna-measurement-cnf
```

## Usage

As a library:

```python
from antenna_measurement_cnf import hello

hello()  # prints "Hello"
```

As a command line tool:

```bash
AntennaMeasurementCNFCli
```

## Development

```bash
pip install -e .[test]
pytest
```

## Project Setup From Scratch

These are the exact steps used to initialize this repository, in case you need to
recreate or re-initialize the project without external assistance.

### 1. Create the package layout

```
cnf/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── antenna_measurement_cnf/
│       ├── __init__.py
│       ├── core.py
│       └── cli.py
└── tests/
    └── test_core.py
```

### 2. Configure `pyproject.toml`

Define the PyPI project name, console script entry point, and git repository URL:

```toml
[project]
name = "antenna-measurement-cnf"

[project.urls]
Repository = "https://github.com/AntennaMeasurement/cnf.git"

[project.scripts]
AntennaMeasurementCNFCli = "antenna_measurement_cnf.cli:main"

[project.optional-dependencies]
test = ["pytest"]
```

### 3. Create a virtual environment and install the package

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[test]"
```

On bash-like shells (Git Bash, WSL, macOS/Linux) use `.venv/Scripts/python`
(Windows) or `.venv/bin/python` (macOS/Linux). On PowerShell, activate the
environment first so `pytest` and the CLI script resolve on `PATH`:

```powershell
.venv\Scripts\Activate.ps1
pytest -v
AntennaMeasurementCNFCli
```

### 4. Run the tests

```bash
.venv/Scripts/python -m pytest -v
```

### 5. Verify the CLI

```bash
.venv/Scripts/AntennaMeasurementCNFCli
```

Expected output: `Hello`

### 6. Initialize git and connect the remote

```bash
git init
git remote add origin https://github.com/AntennaMeasurement/cnf.git
git branch -M main
git add -A
git commit -m "Initial commit: antenna-measurement-cnf package scaffold"
```

### 7. Push to GitHub (when ready)

```bash
git push -u origin main
```

### 8. Publish to PyPI (when ready)

```bash
.venv/Scripts/python -m pip install build twine
.venv/Scripts/python -m build
.venv/Scripts/python -m twine upload dist/*
```
