from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# user profile
# first name, last name, 
# description
# email
# contact info
# current location
class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        image = models.ImageField(default='defaultProfileImg.png', upload_to='_profile_img', blank=True, null=True)
        first_name = models.CharField(max_length=60, blank=True)
        last_name = models.CharField(max_length=60, blank=True)
        description = models.CharField(max_length=60, blank=True)
        mobile = models.CharField(max_length=60, blank=True)
        current_location = models.CharField(max_length=60, blank=True)
        
