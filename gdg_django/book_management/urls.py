from django.urls import path
from . import views


urlpatterns = [
    path("authors/", views.get_authors),
    path("authors/<int:id>/", views.get_author),
    path("authors/create/", views.create_author),
    path("authors/<indt:id>/update/", views.update_author),
    path("authors/<int:id>/delete/", views.delete_author),
    path("authors/<int:id>/books/", views.get_author_books),
    path("authors/book-count/", views.get_author_book_count),
    # book related actions
    path("books/", views.get_books),
    path("books/<int:id>/", views.get_book),
    path("books/create/", views.create_book),
    path("books/<int:id>/update/", views.update_book),
    path("books/<int:id>/delete", views.delete_book),
]
