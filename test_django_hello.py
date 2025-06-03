"""
Tests for Django hello world functionality.
"""
import os
import django
from django.test import TestCase, Client
from django.http import HttpRequest
from core.views import hello_world

# Configure Django settings for tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()


def test_hello_world_view():
    """Test that the hello world view returns the expected content."""
    request = HttpRequest()
    response = hello_world(request)
    
    content = response.content.decode()
    assert response.status_code == 200
    assert "Welcome to Bee Manager" in content
    assert "Hello World!" in content
    assert "bee management system" in content
    print("✓ Hello world view test passed")


def test_hello_world_url():
    """Test that the hello world URL is accessible."""
    client = Client()
    response = client.get('/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "Welcome to Bee Manager" in content
    print("✓ Hello world URL test passed")


if __name__ == "__main__":
    test_hello_world_view()
    test_hello_world_url()
    print("All Django tests passed!")