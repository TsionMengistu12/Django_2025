from django.urls import path
from . import views
from .views import AddLoan


urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.list_books, name="list_books"),
    path("books/<int:book_id>/loan/", AddLoan.as_view(), name="add-loan"),
    path("books/never-loaned/", views.books_never_loaned),
    path("books/newton-science/", views.science_newton_books),
    path("members/top/", views.top_members),
    path("categories/count/", views.books_per_category),
]
