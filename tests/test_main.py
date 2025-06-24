import subprocess
import os
import time
import sys
import platform

def test_main_script_runs_and_logs():
    # Remove old log if exists
    log_file = 'dq_checker.log'
    if os.path.exists(log_file):
        os.remove(log_file)
    # Detect the venv python executable for any OS
    if platform.system() == 'Windows':
        venv_python = os.path.join(os.path.dirname(__file__), '..', 'venv', 'Scripts', 'python.exe')
    else:
        venv_python = os.path.join(os.path.dirname(__file__), '..', 'venv', 'bin', 'python')
    # Run the main script in the correct working directory
    result = subprocess.run([venv_python, 'main.py'], capture_output=True, text=True, cwd=os.path.dirname(__file__) + '/..')
    # Wait a moment for logging to flush
    time.sleep(1)
    # Check that the log file was created and contains expected output
    log_path = os.path.join(os.path.dirname(__file__), '..', log_file)
    assert os.path.exists(log_path), f"Log file not found. stdout: {result.stdout} stderr: {result.stderr}"
    with open(log_path, 'r') as f:
        log_content = f.read()
    # Check for at least one rule name in the log
    assert 'DUPLICATE_CHECK' in log_content or 'NULL_CHECK' in log_content
    # Check that the script did not crash
    assert result.returncode == 0
