from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class TwitterUser(models.Model):
    display_name = models.CharField(max_length=30)
    joined_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.display_name} - {self.joined_date}"
