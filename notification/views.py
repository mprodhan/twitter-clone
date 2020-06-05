from django.shortcuts import HttpResponseRedirect, render, reverse

from notification.models import Notification
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from tweet.views import tweetadd

def visible_tweet(request, id):
    notif = Notification.objects.get(id=id)
    notif.message_visibility = False
    return HttpResponseRedirect(reverse("homepage"), kwargs={"id": notif.target_user.id})

def invisible_tweet(request, id):
    notif = Notification.objects.get(id=id)
    notif.message_visibility = True
    return HttpResponseRedirect(reverse("homepage"), kwargs={"id": notif.target_user.id})