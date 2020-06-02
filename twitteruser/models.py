from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=30)
    joined_date = models.DateTimeField(default=timezone.now)
    # twitter_following = models.ManyToManyField("self", symmetrical=False)

    def __str__(self):
        return self.username
