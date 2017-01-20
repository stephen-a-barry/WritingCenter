from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Story(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
