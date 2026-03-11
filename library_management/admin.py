from django.contrib import admin
from .models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    # shown in the admin list
    list_display = ("title", "author", "available_copies")

    # sidebar filters
    list_filter = ("author", "category")

    # search bar
    search_fields = ("title", "isbn")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Category)
