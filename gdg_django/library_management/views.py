from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from datetime import date
from .models import Book, Loan, Member, Category
from django.db.models import Count


def home(request):
    return HttpResponse("Library Management System")


# FBV that displays the books, their authors and categories
def list_books(request):
    books = Book.objects.all()

    # result = ""
    data = []

    for book in books:
        authors = book.author.name
        categories = ", ".join([c.category for c in book.category.all()])

        data.append(
            {
                "Title": book.title,
                "Author": authors,
                "Categories": categories,
            }
        )

        # result += f"Title: {book.title}<br>"
        # result += f"Author: {authors}<br>"
        # result += f"Categories: {categories}<br> <br>"

    # return HttpResponse(result)
    return JsonResponse(data, safe=False)


# CBV POST request adding new loan for a member
class AddLoan(View):
    def get(self, request):
        return HttpResponse(
            "Use POST to create a loan with member_id, book_id, and optional loan_date (YYYY-MM-DD)."
        )

    def post(self, request):
        member_id = request.POST.get("member_id")
        book_id = request.POST.get("book_id")
        loan_date = request.POST.get("loan_date") or date.today()

        if not member_id or not book_id:
            return JsonResponse(
                {"error": "member_id and book_id are required"}, status=400
            )

        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)
        except (Member.DoesNotExist, Book.DoesNotExist):
            return JsonResponse({"error": "Invalid member_id or book_id"}, status=404)

        loan = Loan.objects.create(loan_date=loan_date, member=member, book=book)

        return JsonResponse(
            {
                "message": "Loan created successfully",
                "member": member.member,
                "book": book.title,
                "loan_id": loan.id,
            }
        )


# Books that have never been loaned
def BooksNeverLoaned(request):
    books = Book.objects.filter(loan__isnull=True)
    result = ""

    for book in books:
        result += f"{book.title}"

    return HttpResponse(result)


# Science category by isaac Newton
def IsaacBook(request):
    books = Book.objects.filter(author__name="Isaac Newton", category__name="Science")
    result = ""

    for book in books:
        result += f"{books.title}<br>"
    return HttpResponse(result)


# Top 3 members with most loans
def MostLoan(request):
    top_members = Member.objects.annotate(loan_count=Count("loan")).order_by(
        "-loan_count"
    )[:3]
    return f"Top 3 members are: {top_members[0].name} - {top_members[0].loan_count}, {top_members[1].name} - {top_members[1].loan_count}, {top_members[2].name} - {top_members[2].loan_count} "


# Number of books in each category
def NumberOfBook(request):
    categories = Category.objects.annotate(book_count=Count("book"))
    result = []

    for category in categories:
        result.append(f"{category.name} : {category.book_count}")

    return HttpResponse(result)
