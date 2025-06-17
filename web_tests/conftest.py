"""
Django test configuration for pytest.
"""
import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    """Configure Django database for testing."""
    # The fixture will be handled by pytest-django automatically
    pass