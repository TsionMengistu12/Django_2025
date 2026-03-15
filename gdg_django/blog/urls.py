from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.Home, name="home"),
    path("welcome/", views.Welcome.as_view(), name="welcome"),
    path("post/", views.AllPosts.as_view(), name="post"),
]
