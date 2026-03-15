from django.urls import path
from . import views
from .views import AddLoan


urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.list_books, name="list_books"),
    path("books/<int:book_id>/loan/", AddLoan.as_view(), name="add-loan"),
    path("books/never-loaned/", views.BooksNeverLoaned),
    path("books/newton-science/", views.IssacBook),
    path("members/top/", views.TopMembers),
    path("categories/count/", views.BooksPerCategory),
]
