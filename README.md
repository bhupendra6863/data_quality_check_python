# Data Quality Checker

A robust, extensible Python tool to check data quality using configurable rules, with full logging and unit/integration test coverage.

## Features
- Modular rule system (null, duplicate, range, starts_with, regex, etc.)
- YAML-based rule configuration
- Logging to both console and file (`dq_checker.log`)
- Unit and integration tests for all components
- Cross-platform support (Windows, macOS, Linux)

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd data_quality_checker
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the data quality checker:**
   ```sh
   python main.py
   ```
5. **Run the tests:**
   ```sh
   pytest
   ```
   All tests (unit and integration) will run and should pass on any OS.

## Project Structure
- `dq_checker/` — Main package with all rule logic and engine
- `data/` — Sample/test data
- `rules/` — YAML rules
- `tests/` — Unit and integration tests (engine, checker, main script)
- `requirements.txt` — All dependencies
- `pytest.ini` — Pytest config for easy test discovery
- `main.py` — Entry point

## Notes
- Log output is written to `dq_checker.log` (ignored by git)
- Add or modify rules in `rules/rules.yaml`
- Add more tests in the `tests/` folder as needed
- The test suite is cross-platform and will auto-detect the correct Python executable for subprocess tests

## Contributing
Pull requests are welcome! Please add or update tests for any new features or bug fixes.
