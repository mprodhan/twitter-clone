from django.urls import path
from tweet import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("tweet/", views.tweetadd),
    path("profile/", views.profileview)
]