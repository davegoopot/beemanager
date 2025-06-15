"""
Tests for Hive and HiveNote views.
"""
import os
import sys
import django
from django.test import TestCase, Client
from django.urls import reverse

# Add parent directory to path so we can import core
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure Django settings for tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from core.models import Hive, HiveNote


class HiveViewTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()
        self.hive1 = Hive.objects.create(name="Hive 1")
        self.hive2 = Hive.objects.create(name="Hive 2")
        HiveNote.objects.create(hive=self.hive1, note_text="First inspection")
        HiveNote.objects.create(hive=self.hive1, note_text="Second inspection")

    def test_hive_list_view(self):
        """Test that the hive list view displays all hives."""
        response = self.client.get('/hives/')
        
        assert response.status_code == 200
        content = response.content.decode()
        assert "Hive 1" in content
        assert "Hive 2" in content
        assert "Bee Manager" in content  # Check for consistent branding
        print("✓ Hive list view test passed")

    def test_hive_detail_view(self):
        """Test that the hive detail view shows hive info and notes."""
        response = self.client.get(f'/hives/{self.hive1.id}/')
        
        assert response.status_code == 200
        content = response.content.decode()
        assert "Hive 1" in content
        assert "First inspection" in content
        assert "Second inspection" in content
        assert "Add Note" in content  # Button to add note
        print("✓ Hive detail view test passed")

    def test_add_note_get(self):
        """Test that the add note form displays correctly."""
        response = self.client.get(f'/hives/{self.hive1.id}/add-note/')
        
        assert response.status_code == 200
        content = response.content.decode()
        assert "Add Note" in content
        assert "Hive 1" in content
        assert 'name="note_text"' in content
        print("✓ Add note GET view test passed")

    def test_add_note_post(self):
        """Test that posting a new note works and redirects."""
        response = self.client.post(f'/hives/{self.hive1.id}/add-note/', {
            'note_text': 'New inspection note'
        })
        
        # Should redirect back to hive detail
        assert response.status_code == 302
        
        # Check that the note was created
        note = HiveNote.objects.filter(note_text='New inspection note').first()
        assert note is not None
        assert note.hive == self.hive1
        print("✓ Add note POST view test passed")

    def test_hive_not_found(self):
        """Test that accessing a non-existent hive returns 404."""
        response = self.client.get('/hives/999/')
        assert response.status_code == 404
        print("✓ Hive not found test passed")


if __name__ == "__main__":
    # Run individual test methods
    import django
    from django.test.utils import get_runner
    from django.conf import settings
    
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    
    # Create test suite
    from unittest import TestLoader, TextTestRunner
    loader = TestLoader()
    suite = loader.loadTestsFromTestCase(HiveViewTest)
    
    runner = TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("All view tests passed!")
    else:
        print("Some tests failed!")