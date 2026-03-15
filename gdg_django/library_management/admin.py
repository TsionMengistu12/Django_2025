from django.contrib import admin
from .models import Book, Author, Category, Member, Loan


class BookAdmin(admin.ModelAdmin):
    # columns shown in admin list
    list_display = ("title", "author", "available_copies")

    # filters shown
    list_filter = ("author", "category")

    # search-bar shown
    search_fields = ("title", "isbn")

    def available(self, obj):
        return obj.is_available()

    available.boolean = True


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Member)
admin.site.register(Loan)
