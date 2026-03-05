from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.hello_blog, name="home"),
    path("welcome/", views.WelcomeView.as_view(), name="welcome"),
    path("posts/", views.list_posts, name="posts"),
]
