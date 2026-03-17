from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post


# Function based view to display hello blog on the home page
def Home(request):
    return HttpResponse("Hello Blog")


# Class based view handles GET request
class Welcome(View):

    def get(self, request):
        return HttpResponse("Welcome to Django CBV")


# FBV that fetches posts and return their titles
class AllPosts(View):
    def AllPosts(request):
        posts = Post.objects.all()

        titles = ""

        for post in posts:
            titles += post.title + "<br>"

        return HttpResponse(titles)
