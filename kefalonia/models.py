from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Youtube(models.Model):
    video = EmbedVideoField()

class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title