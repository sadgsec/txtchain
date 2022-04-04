from django.db import models
from django.utils import timezone
# Create your models here.


class Thread(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted = models.DateTimeField(default=timezone.now())

class Response(models.Model):
    body = models.TextField()
    posted = models.DateTimeField(default=timezone.now())

