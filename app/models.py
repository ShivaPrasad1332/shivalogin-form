from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    Profile_Pic=models.ImageField(upload_to='Profile_Pic')

