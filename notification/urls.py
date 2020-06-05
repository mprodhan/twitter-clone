from django.urls import path
from notification import views

urlpatterns = [
    path("visibletweet/<int:id>", views.visible_tweet),
    path("invisibletweet/<int:id>", views.invisible_tweet)
]