from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def default_time():
    return timezone.now()
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User,related_name='post', on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(default=default_time)

# Create your models here.
