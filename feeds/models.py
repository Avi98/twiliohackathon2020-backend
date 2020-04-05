from django.db import models
from django.utils import timezone

def default_time():
    return timezone.now()
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=default_time)

# Create your models here.
