
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=50)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.title
