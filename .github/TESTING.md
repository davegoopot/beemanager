# Testing with pytest

This project uses [pytest](https://pytest.org/) as the unit testing framework. This document provides instructions for running tests, writing tests, and following testing best practices.

## Prerequisites

- Python 3.13 or higher
- [UV](https://docs.astral.sh/uv/) package manager

## Installation

1. Install UV if not already installed:
   ```bash
   pip install uv
   ```

2. Set up the development environment:
   ```bash
   uv sync
   ```

This will install pytest and all other development dependencies.

## Running Tests

### Run All Tests

```bash
uv run pytest
```

### Run Tests with Verbose Output

```bash
uv run pytest -v
```

### Run Specific Test File

```bash
uv run pytest tests/test_dummy.py
```

### Run Specific Test Function

```bash
uv run pytest tests/test_dummy.py::test_dummy_that_should_pass
```

### Run Tests with Coverage (if available)

```bash
uv run pytest --cov
```

## Test Configuration

The project's pytest configuration is defined in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
```

## Writing Tests

### Test File Structure

- All test files should be placed in the `tests/` directory
- Test files should be named with the pattern `test_*.py` or `*_test.py`
- Test functions should be named with the pattern `test_*`

### Test-Driven Development (TDD)

This project follows Test-Driven Development practices:

1. **Write a failing test** before implementing a feature
2. **Run the test** to confirm it fails
3. **Write the minimum code** necessary to pass the test
4. **Run the tests again** to ensure all tests pass
5. **Refactor** the code if necessary, ensuring tests still pass

### Example Test Structure

```python
def test_function_returns_expected_value():
    # Arrange
    input_value = "test_input"
    expected_output = "expected_result"
    
    # Act
    result = function_under_test(input_value)
    
    # Assert
    assert result == expected_output
```

### Test Naming Conventions

Use descriptive test function names that clearly indicate what is being tested:

```python
def test_given_valid_input_returns_correct_output():
    pass

def test_given_invalid_input_raises_value_error():
    pass

def test_burster_takes_correct_number_of_pictures():
    pass
```

### Mock Objects and Test Doubles

For testing components that have external dependencies (like camera hardware), use mock objects:

```python
class DummyCamera:
    def __init__(self):
        self.picture_count = 0
        self.picture_filenames = []

    def capture_file(self, filename):
        self.picture_count += 1
        self.picture_filenames.append(filename)
```

## Test Categories

### Unit Tests

Test individual functions and methods in isolation.

### Integration Tests

Test the interaction between multiple components.

### Dummy Tests

The project includes dummy tests (`tests/test_dummy.py`) that serve as examples and ensure the testing framework is working correctly.

## Continuous Integration

Tests are automatically run on every push and pull request via GitHub Actions. The workflow:

- Runs on Python 3.13
- Installs dependencies using pip and pytest
- Executes the test suite
- Excludes hardware-dependent tests (like `test_burst.py`) that require specific hardware

## Troubleshooting

### Import Errors

If you encounter import errors when running tests, ensure:

1. All dependencies are installed: `uv sync`
2. You're running tests from the project root directory
3. The virtual environment is activated (UV handles this automatically)

### Hardware-Dependent Tests

Some tests (like camera-related tests) may require specific hardware or additional dependencies. These tests are excluded from CI/CD pipelines but can be run locally with appropriate setup.

### Adding New Dependencies

When adding new test dependencies:

1. Add them to the `dev` dependency group in `pyproject.toml`:
   ```toml
   [dependency-groups]
   dev = [
       "pytest>=8.3.4",
       "new-test-dependency>=1.0.0",
   ]
   ```

2. Run `uv sync` to install the new dependencies

## Best Practices

1. **Write self-documenting test names** - avoid comments when the function name is clear
2. **One assertion per test** when possible
3. **Use meaningful test data** rather than generic values
4. **Test edge cases** and error conditions
5. **Keep tests independent** - each test should be able to run in isolation
6. **Clean up after tests** - ensure tests don't leave behind files or state

## Getting Help

- [pytest documentation](https://docs.pytest.org/)
- [UV documentation](https://docs.astral.sh/uv/)
- Project-specific testing questions can be raised in GitHub issues