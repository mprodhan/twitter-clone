from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser

class Tweet(models.Model):
    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.twittteruser} - {self.tweet}"


