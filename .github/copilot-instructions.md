# Environment Setup

In agentic mode, start each session by installing Astral UV:

```bash
pip install uv
```

All tasks in this project require UV for dependency management and virtual environments.

# Coding Approach

1. *Use test-driven development (TDD)*
  a. Write a failing test before writing the code to implement a feature. Only write one test at a time before checking that it fails
  b. Run the test
  c. Write the minimum code necessary to pass the test.
  d. Run the tests again to ensure all tests pass.
  e. Refactor the code if necessary, ensuring that all tests still pass.

2. Prefer using Python at the latest supported version.

3. Use Astral UV tools for managing dependencies and virtual environments. 
  a. For sinlge file scripts use the Astral UV script headers to manage dependencies and python version.

4. Try not to write comments. Instead prefer to write self-documenting code that is clear and easy to understand. If a function is called `test_get_nginx_version_uses_custom_certificate` do not write a comment that says `# Test that get_nginx_version uses custom certificate`. Instead, the function name itself should be clear enough to understand what it does.

# Testing with pytest

This project uses [pytest](https://pytest.org/) as the unit testing framework.
                  # 

## Test Configuration

The project's pytest configuration is in `pyproject.toml`

## Writing Tests

### Test Structure
- Place test files in `tests/` directory
- Name test files with pattern `test_*.py` or `*_test.py`
- Name test functions with pattern `test_*`

### Test Naming Conventions
Use descriptive names that clearly indicate what is being tested:

```python
def test_given_valid_input_returns_correct_output():
    pass

def test_given_invalid_input_raises_value_error():
    pass

def test_burster_takes_correct_number_of_pictures():
    pass
```


  