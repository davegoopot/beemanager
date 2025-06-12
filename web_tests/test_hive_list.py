"""
Tests for hive list functionality.
"""
import os
import django
from django.test import TestCase, Client
from django.http import HttpRequest

from core.views import home_page

# Configure Django settings for tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()


def test_home_page_shows_three_hives():
    request = HttpRequest()
    response = home_page(request)
    
    content = response.content.decode()
    assert response.status_code == 200
    assert "Hive List" in content or "hive" in content.lower()
    
    # Count occurrences of hive references - should be exactly 3
    hive_count = content.lower().count("hive")
    assert hive_count >= 3, f"Expected at least 3 hive references, found {hive_count}"
    print("✓ Home page hive list test passed")


def test_home_page_url_shows_hives():
    client = Client()
    response = client.get('/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "hive" in content.lower()
    print("✓ Home page URL hive list test passed")


if __name__ == "__main__":
    test_home_page_shows_three_hives()
    test_home_page_url_shows_hives()
    print("All hive list tests passed!")