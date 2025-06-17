"""
Tests for Hive and HiveNote models.
"""
import pytest
from core.models import Hive, HiveNote


@pytest.mark.django_db
def test_create_hive():
    """Test that a hive can be created with a name."""
    hive = Hive.objects.create(name="Hive 1")
    assert hive.name == "Hive 1"
    assert str(hive) == "Hive 1"


@pytest.mark.django_db
def test_hive_str_representation():
    """Test the string representation of a hive."""
    hive = Hive(name="Test Hive")
    assert str(hive) == "Test Hive"


@pytest.mark.django_db
def test_create_hive_note():
    """Test that a hive note can be created with text and automatic timestamp."""
    hive = Hive.objects.create(name="Test Hive")
    note = HiveNote.objects.create(hive=hive, note_text="First inspection - all looks good")
    
    assert note.hive == hive
    assert note.note_text == "First inspection - all looks good"
    assert note.created_at is not None


@pytest.mark.django_db
def test_hive_note_str_representation():
    """Test the string representation of a hive note."""
    hive = Hive(name="Test Hive")
    note = HiveNote(hive=hive, note_text="Test note", created_at="2023-01-01")
    expected = "Test Hive - 2023-01-01: Test note"
    assert str(note) == expected


@pytest.mark.django_db
def test_hive_notes_relationship():
    """Test that hive notes are properly related to hives."""
    hive = Hive.objects.create(name="Test Hive")
    note1 = HiveNote.objects.create(hive=hive, note_text="First note")
    note2 = HiveNote.objects.create(hive=hive, note_text="Second note")
    
    hive_notes = hive.hivenote_set.all()
    assert len(hive_notes) == 2
    assert note1 in hive_notes
    assert note2 in hive_notes

