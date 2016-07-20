from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    image = models.ImageField(blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
