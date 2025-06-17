"""
Django test configuration for pytest.

The web tests require Django database access. The pytest.ini file is configured
with --create-db to ensure that pytest-django automatically creates and migrates
the test database before running tests.
"""
import pytest