"""
Test for the serve.bash script.
"""

import os
import stat
import subprocess


def test_serve_script_exists():
    """Test that serve.bash script exists in the root directory."""
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "serve.bash")
    assert os.path.exists(script_path), "serve.bash script should exist in the root directory"


def test_serve_script_is_executable():
    """Test that serve.bash script is executable."""
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "serve.bash")
    assert os.path.exists(script_path), "serve.bash script should exist"
    
    file_stats = os.stat(script_path)
    is_executable = bool(file_stats.st_mode & stat.S_IEXEC)
    assert is_executable, "serve.bash script should be executable"


def test_serve_script_contains_correct_command():
    """Test that serve.bash script contains the correct Django command."""
    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "serve.bash")
    assert os.path.exists(script_path), "serve.bash script should exist"
    
    with open(script_path, 'r') as f:
        content = f.read()
    
    assert "uv run python manage.py runserver 0.0.0.0:8335" in content, "Script should run Django server on port 8335"
    assert "#!/bin/bash" in content, "Script should have bash shebang"