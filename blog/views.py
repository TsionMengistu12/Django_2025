from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# This is for the class based view
from django.views import View
from django.http import HttpRequest


def hello_blog(request):
    return HttpResponse("Hello Blog")


def list_posts(request):

    posts = Post.objects.all()
    # we iterate over the posts to extract the titles
    titles = ""
    for post in posts:
        titles += post.title + "<br>"

    return HttpResponse(titles)


# class based view
class WelcomeView(View):

    def get(self, request):
        return HttpRequest("Welcome to Django CBV")
