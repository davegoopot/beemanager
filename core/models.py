from django.db import models
from django.utils import timezone


class Hive(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class HiveNote(models.Model):
    hive = models.ForeignKey(Hive, on_delete=models.CASCADE)
    note_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.hive.name} - {self.created_at}: {self.note_text}"

    class Meta:
        ordering = ['-created_at']  # Most recent first