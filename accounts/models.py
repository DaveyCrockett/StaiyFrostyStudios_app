from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    CHOICES = [('Artist', 'Artist'), ('Programmer', 'Programmer')]
    role = models.CharField(max_length=12, choices=CHOICES, blank=True, null=True)
