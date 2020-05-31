from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser
from tweet.models import Tweet

class Notification(models.Model):
    target_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    date_post = models.DateTimeField(default=timezone.now)
    message_visibility = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.target_user} - {self.tweet}"
