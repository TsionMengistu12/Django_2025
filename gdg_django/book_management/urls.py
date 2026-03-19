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
    path("books/<int:id>/delete/", views.delete_book),
    # category related actions
    path("category/", views.get_categories),
    path("category/<int:id>/", views.get_category),
    path("category/create/", views.create_category),
    path("category/<int:id>/update/", views.update_category),
    path("category/<int:id>/delete/", views.delete_category),
    # filtering functional endpoints
    path("books/author/<int:author_id>/", views.get_book_by_author),
    path("books/category/<int:category_id>/", views.get_book_by_category),
    path("books/search/?q=<title>/", views.search_book_title),
    path("books/price-range/?min=<value>&max=<value>/", views.filter_price),
    path("books/avilable/", views.available_books),
    path("books/order-by-date/", views.order_published_date),
    path("books/top-5/", views.top_five_books),
]
