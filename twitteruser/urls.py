from django.urls import path
from twitteruser import views

urlpatterns = [
    path("following/<int:id>/", views.following),
    path("unfollow/<int:id>/", views.unfollow)
]