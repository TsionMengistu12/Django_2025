from django.shortcuts import render
from .models import Book, Author, Category
from django.http import HttpResponse


def Show(request):

    authors = Author.objects.all()

    author = ""
    for a in authors:
        author += authors.name + "<br>"

    return HttpResponse(author)
