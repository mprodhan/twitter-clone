from django.urls import path
from tweet import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("tweetdetail/<int:id>/", views.tweet_detail),
    path("tweet/", views.tweetadd),
    path("tweet/edit/<int:id>/", views.tweet_edit),
    path("user/<int:id>/", views.user_detail),
    path("profile/", views.profileview)
]