from django.shortcuts import render, reverse, HttpResponseRedirect
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from tweet.forms import TweetPost

def index(request):
    tweetdata = Tweet.objects.all()
    return render(request, "index.html", {"tweetdata": tweetdata})

def tweetadd(request):
    if request.method == "POST":
        form = TweetPost(request.POST)
        if form.is_valid():
            tweetpost = form.cleaned_data
            twitteruser = TwitterUser.objects.get(id=request.user.id)
            Tweet.objects.create(
                tweet = tweetpost["tweet"],
                twitteruser = twitteruser
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = TweetPost()
    return render(request, "tweets.html" , {"form": form})

def profileview(request):
    twitteruser = TwitterUser.objects.get(id=request.user.id)
    tweets = Tweet.objects.all()
    return render(request, "profile.html", {"twitteruser": twitteruser, "tweets": tweets})

def user_detail(request, id):
    twitteruser = TwitterUser.objects.get(id=id)
    tweets = Tweet.objects.filter(twitteruser=twitteruser)
    return render(request, "profile.html", {"twitteruser": twitteruser, "tweets": tweets})

def tweet_edit(request, id):
    tweet = Tweet.objects.get(id=id)
    if request.method == "POST":
        form = TweetPost(request.POST, instance=tweet)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = TweetPost(instance=tweet)
    return render(request, "tweets.html", {"form": form})


