from django.shortcuts import render, reverse, HttpResponseRedirect
from twitteruser.models import TwitterUser
from tweet.models import Tweet


def following(request, id):
    following = TwitterUser.objects.get(id=id)
    request.user.twitter_following.add(following)
    return HttpResponseRedirect(reverse("homepage"))

def unfollow(request, id):
    unfollow = TwitterUser.objects.get(id=id)
    request.user.twitter_following.remove(unfollow)
    return HttpResponseRedirect(reverse("homepage"))
