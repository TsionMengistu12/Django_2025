from django.db import models


# The author table
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# The category table
class Category(models.Model):
    c_name = models.CharField(max_length=200)

    def __str__(self):
        return self.c_name


# The member table
class Member(models.Model):
    m_name = models.CharField(max_length=200)

    def __str__(self):
        return self.m_name


# The book table
class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    available_copies = models.IntegerField()

    # many to many relation: one book can belong to many categories
    category = models.ManyToManyField(Category)

    # one to many relation: one book can have many authors
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# The loan table
class Loan(models.Model):
    loan_date = models.DateField()

    # many to one relation: one member can have multiple loans
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    # one to many relation: one book can have many loans
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member} borrowed {self.book}"
