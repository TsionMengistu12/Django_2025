from django.db import models


# The Author table
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=70)
    date_of_bith = models.DateField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# The category table
class Category(models.Model):
    c_name = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name


# The Book table
class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
