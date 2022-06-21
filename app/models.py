from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.created.strftime('%d-%m-%Y')}"