# Contributing

Thank you for your interest in contributing to this project.

## How to contribute

1. Fork the repository and create a branch for your change.
2. Install dependencies using:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Make your changes and run the workflow locally:
   ```powershell
   python multi_agent_accounting_ai_runner.py
   ```
4. Commit with a clear message and open a pull request.

## Development notes

- The runner exports outputs in the `data/` folder.
- Generated files are ignored by `.gitignore`.
- If you add dependencies, update `requirements.txt`.

## Pull request checklist

- [ ] Code runs successfully with Python 3.11.
- [ ] No generated artifacts are added to the repository.
- [ ] `README.md` is updated if behavior changes.
