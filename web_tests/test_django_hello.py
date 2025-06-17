"""
Tests for Django hello world functionality.
"""
import pytest
from django.test import Client
from django.http import HttpRequest

from core.views import hello_world


@pytest.mark.django_db
def test_hello_world_view():
    """Test that the hello world view returns the expected content."""
    request = HttpRequest()
    response = hello_world(request)
    
    content = response.content.decode()
    assert response.status_code == 200
    assert "Welcome to Bee Manager" in content
    assert "Hello World!" in content
    assert "bee management system" in content


@pytest.mark.django_db
def test_hello_world_url():
    """Test that the hello world URL is accessible."""
    client = Client()
    response = client.get('/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "Welcome to Bee Manager" in content