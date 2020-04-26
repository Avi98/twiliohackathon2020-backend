from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sup_price= models.DecimalField(max_digits=10, decimal_places=2)
    selling_price= models.DecimalField(max_digits=10, decimal_places=2)
    margin= models.IntegerField(blank=True, null=True)
    name= models.CharField(max_length=50)
    manufacture= models.CharField(max_length=50, null=True, blank=True)
    description= models.CharField(max_length=50)
    onSale= models.BooleanField(default=True, blank=True)
    image1 = models.ImageField(default='defaultProfileImg.png', upload_to='_profile_img', blank=False, null=False)
    image2 = models.ImageField(default='defaultProfileImg.png', upload_to='_profile_img', blank=True, null=True)
    image3 = models.ImageField(default='defaultProfileImg.png', upload_to='_profile_img', blank=True, null=True)
