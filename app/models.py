from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return f"{self.created.strftime('%d-%m-%Y')}"
    def __str__(self):
        return f"{self.user.username}"


class Nanny(models.Model):
    profile_pic = models.ImageField(
        upload_to='profilepic/', default='default.jpeg')
    name = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=50, blank=True)
    rates = models.IntegerField(blank=True)
    availability =  models.BooleanField(max_length=50, blank=True)
    age =  models.IntegerField(blank=True)
    location =  models.CharField(max_length=50, blank=True)
    about = models.TextField(default="Some String")
    skills = models.TextField(default="Some String")

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images


class Bio(models.Model):
    about = models.TextField()
    skills = models.TextField()
