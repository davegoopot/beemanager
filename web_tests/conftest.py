"""
Django test configuration for pytest.
"""
import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    """Configure Django database for testing."""
    pass