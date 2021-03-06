from accounts.models import CustomUser
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='static/images/profile_pictures/', default='static/images/profile_pictures/dummy-picture.jpg', blank=True)
    resume = models.FileField(upload_to='static/documents/resume/', blank=True)
    followers = models.ManyToManyField(CustomUser, blank=True, related_name='followers')