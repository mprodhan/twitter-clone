from django import forms
from tweet.models import Tweet

class TweetPost(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet']