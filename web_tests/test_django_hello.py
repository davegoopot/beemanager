"""
Tests for Django hello world functionality.
"""
import os
import sys
import django
from django.test import TestCase, Client
from django.http import HttpRequest

# Add parent directory to path so we can import core
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.views import home_page

# Configure Django settings for tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()


def test_hello_world_view():
    """Test that the home page view returns the expected content."""
    request = HttpRequest()
    response = home_page(request)
    
    content = response.content.decode()
    assert response.status_code == 200
    assert "Bee Manager" in content
    assert "hive" in content.lower()  # Updated to check for hive content instead
    print("✓ Hello world view test passed")


def test_hello_world_url():
    """Test that the home page URL is accessible."""
    client = Client()
    response = client.get('/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "Bee Manager" in content
    print("✓ Hello world URL test passed")


if __name__ == "__main__":
    test_hello_world_view()
    test_hello_world_url()
    print("All Django tests passed!")