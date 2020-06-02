from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.TextField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tweet


