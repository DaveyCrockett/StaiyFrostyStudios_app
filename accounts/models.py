from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    department = models.CharField(max_length=512,null=True, blank=True)
    role = models.CharField(max_length=256, blank=True, null=True)
