"""
Tests for Hive and HiveNote views.
"""
import pytest
from django.test import Client

from core.models import Hive, HiveNote


@pytest.fixture
def client():
    """Client fixture for making HTTP requests."""
    return Client()


@pytest.fixture
def sample_hives():
    """Create sample hives with notes for testing."""
    hive1 = Hive.objects.create(name="Hive 1")
    hive2 = Hive.objects.create(name="Hive 2")
    HiveNote.objects.create(hive=hive1, note_text="First inspection")
    HiveNote.objects.create(hive=hive1, note_text="Second inspection")
    return hive1, hive2


@pytest.mark.django_db
def test_hive_list_view(client, sample_hives):
    """Test that the hive list view displays all hives."""
    response = client.get('/hives/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "Hive 1" in content
    assert "Hive 2" in content
    assert "Bee Manager" in content  # Check for consistent branding


@pytest.mark.django_db
def test_hive_detail_view(client, sample_hives):
    """Test that the hive detail view shows hive info and notes."""
    hive1, _ = sample_hives
    response = client.get(f'/hives/{hive1.id}/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "Hive 1" in content
    assert "First inspection" in content
    assert "Second inspection" in content
    assert "Add Note" in content  # Button to add note


@pytest.mark.django_db
def test_add_note_get(client, sample_hives):
    """Test that the add note form displays correctly."""
    hive1, _ = sample_hives
    response = client.get(f'/hives/{hive1.id}/add-note/')
    
    assert response.status_code == 200
    content = response.content.decode()
    assert "Add Note" in content
    assert "Hive 1" in content
    assert 'name="note_text"' in content


@pytest.mark.django_db
def test_add_note_post(client, sample_hives):
    """Test that posting a new note works and redirects."""
    hive1, _ = sample_hives
    response = client.post(f'/hives/{hive1.id}/add-note/', {
        'note_text': 'New inspection note'
    })
    
    # Should redirect back to hive detail
    assert response.status_code == 302
    
    # Check that the note was created
    note = HiveNote.objects.filter(note_text='New inspection note').first()
    assert note is not None
    assert note.hive == hive1


@pytest.mark.django_db
def test_hive_not_found(client):
    """Test that accessing a non-existent hive returns 404."""
    response = client.get('/hives/999/')
    assert response.status_code == 404

