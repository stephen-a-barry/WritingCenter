from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
# If you change fields here, it is necessary to migrate again
class Entry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.title
