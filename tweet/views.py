import re

from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib.auth.decorators import login_required

from notification.models import Notification
from tweet.forms import TweetPost
from tweet.models import Tweet
from twitteruser.models import TwitterUser

@login_required
def index(request):
    tweetdata = Tweet.objects.all()
    return render(request, "index.html", {"tweetdata": tweetdata})

# Assistance from Peter with the Notification creation piece
@login_required
def tweetadd(request):
    if request.method == "POST":
        form = TweetPost(request.POST)
        if form.is_valid():
            tweetpost = form.cleaned_data
            twitteruser = TwitterUser.objects.get(id=request.user.id)
            tweet = Tweet.objects.create(
                tweet = tweetpost["tweet"],
                twitteruser = twitteruser
            )
            if "@" in tweet.tweet:
                usernames = re.findall(r"@(\w+)", tweet.tweet)
                for user in usernames:
                    t = TwitterUser.objects.get(username=user)
                    notification = Notification.objects.create(
                        tweet = tweet,
                        target_user = t
                    )
            return HttpResponseRedirect(reverse("homepage"))
    form = TweetPost()
    return render(request, "tweets.html" , {"form": form})

@login_required
def profileview(request):
    twitteruser = TwitterUser.objects.get(id=request.user.id)
    tweets = Tweet.objects.all()
    return render(request, "profile.html", {"twitteruser": twitteruser, "tweets": tweets})

def user_detail(request, id):
    twitteruser = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(twitteruser=twitteruser)
    return render(request, "profile.html", {"twitteruser": twitteruser, "tweets": tweets})

def tweet_detail(request, id):
    tweet = Tweet.objects.get(id=id)
    return render(request, "tweetdetail.html", {"tweet": tweet})

@login_required
def tweet_edit(request, id):
    tweet = Tweet.objects.get(id=id)
    if request.method == "POST":
        form = TweetPost(request.POST, instance=tweet)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = TweetPost(instance=tweet)
    return render(request, "tweets.html", {"form": form})

