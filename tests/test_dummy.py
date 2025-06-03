"""
    Dummy test file with intentionally failing test as requested in the issue.
"""


def test_dummy_that_should_fail():
    """
    This is a dummy test that intentionally fails.
    This was added as requested in the issue to demonstrate the pytest framework setup.
    """
    assert False, "This dummy test is supposed to fail as requested in the issue"


def test_dummy_that_should_pass():
    """
    This is a dummy test that passes to show the framework works.
    """
    assert True, "This dummy test should pass"