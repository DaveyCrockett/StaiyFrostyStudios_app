from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Message(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    creator = models.ForeignKey(
        get_user_model(),
        to_field="username",
        on_delete=models.CASCADE,
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('message_detail', args=[self.id])
