"""
Tests for Hive and HiveNote models.
"""
import os
import sys
import django
from django.test import TestCase

# Add parent directory to path so we can import core
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configure Django settings for tests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from core.models import Hive, HiveNote


class HiveModelTest(TestCase):
    def test_create_hive(self):
        """Test that a hive can be created with a name."""
        hive = Hive.objects.create(name="Hive 1")
        assert hive.name == "Hive 1"
        assert str(hive) == "Hive 1"
        print("✓ Hive creation test passed")

    def test_hive_str_representation(self):
        """Test the string representation of a hive."""
        hive = Hive(name="Test Hive")
        assert str(hive) == "Test Hive"
        print("✓ Hive string representation test passed")


class HiveNoteModelTest(TestCase):
    def test_create_hive_note(self):
        """Test that a hive note can be created with text and automatic timestamp."""
        hive = Hive.objects.create(name="Test Hive")
        note = HiveNote.objects.create(hive=hive, note_text="First inspection - all looks good")
        
        assert note.hive == hive
        assert note.note_text == "First inspection - all looks good"
        assert note.created_at is not None
        print("✓ HiveNote creation test passed")

    def test_hive_note_str_representation(self):
        """Test the string representation of a hive note."""
        hive = Hive(name="Test Hive")
        note = HiveNote(hive=hive, note_text="Test note", created_at="2023-01-01")
        expected = "Test Hive - 2023-01-01: Test note"
        assert str(note) == expected
        print("✓ HiveNote string representation test passed")

    def test_hive_notes_relationship(self):
        """Test that hive notes are properly related to hives."""
        hive = Hive.objects.create(name="Test Hive")
        note1 = HiveNote.objects.create(hive=hive, note_text="First note")
        note2 = HiveNote.objects.create(hive=hive, note_text="Second note")
        
        hive_notes = hive.hivenote_set.all()
        assert len(hive_notes) == 2
        assert note1 in hive_notes
        assert note2 in hive_notes
        print("✓ Hive notes relationship test passed")


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
    suite = loader.loadTestsFromTestCase(HiveModelTest)
    suite.addTests(loader.loadTestsFromTestCase(HiveNoteModelTest))
    
    runner = TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("All model tests passed!")
    else:
        print("Some tests failed!")