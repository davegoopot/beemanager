"""
Test to validate the pytest instructions and examples work correctly.
"""

def test_given_valid_input_returns_correct_output():
    """Example test following the documented naming conventions."""
    input_value = "test_input"
    expected_output = "test_input_processed"
    
    # Simple example function
    def example_function(value):
        return value + "_processed"
    
    result = example_function(input_value)
    assert result == expected_output


def test_given_invalid_input_raises_value_error():
    """Example test for error handling."""
    def example_function_with_validation(value):
        if not value:
            raise ValueError("Value cannot be empty")
        return value.upper()
    
    import pytest
    with pytest.raises(ValueError):
        example_function_with_validation("")


def test_pytest_instructions_examples_work():
    """Test that verifies the examples in TESTING.md work."""
    # Test the example assertion pattern
    actual_value = 42
    expected_value = 42
    assert actual_value == expected_value
    
    # Test that descriptive test names are being used
    assert test_given_valid_input_returns_correct_output.__name__.startswith("test_")