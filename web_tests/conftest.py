"""
Django test configuration for pytest.
"""
import os
import django
from django.conf import settings
from django.test.utils import get_runner

def pytest_configure():
    """Configure Django settings for pytest."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    django.setup()