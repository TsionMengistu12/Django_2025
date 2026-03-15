from django.db import models


# The author table
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# The Member table
class Member(models.Model):
    member = models.CharField(max_length=200)

    def __str__(self):
        return self.member


# The category table
class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


# The Book table
class Book(models.Model):
    title = models.CharField((""), max_length=200)
    available_copies = models.IntegerField()
    isbn = models.CharField(max_length=13)

    # many to many relationship: one book can have many categories
    category = models.ManyToManyField(Category)

    # one to many: one author can write many books
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def is_available(self):
        return not self.loan_set.exists()

    def __str__(self):
        return self.title


# The Loan table
class Loan(models.Model):

    loan_date = models.DateField()

    # one member can have many loans
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    # one book can have many loans
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member} borrowed {self.book} "
