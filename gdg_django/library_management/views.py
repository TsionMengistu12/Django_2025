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
    def get(self, request, book_id=None):
        return HttpResponse(
            "Use POST to create a loan with member_id, book_id, and optional loan_date (YYYY-MM-DD)."
        )

    def post(self, request, book_id=None):
        member_id = request.POST.get("member_id")
        selected_book_id = book_id or request.POST.get("book_id")
        loan_date = request.POST.get("loan_date") or date.today()

        if not member_id or not selected_book_id:
            return JsonResponse(
                {"error": "member_id and book_id are required"}, status=400
            )

        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=selected_book_id)
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
    result = [{"title": book.title} for book in books]
    return JsonResponse(result, safe=False)


# Science category by isaac Newton
def IssacBook(request):
    books = Book.objects.filter(
        author__name="Isaac Newton", category__category="Science"
    )
    result = [{"title": book.title} for book in books]
    return JsonResponse(result, safe=False)


# Top 3 members with most loans
def TopMembers(request):
    top_members = Member.objects.annotate(loan_count=Count("loan")).order_by(
        "-loan_count"
    )[:3]
    result = [
        {"member": member.member, "loan_count": member.loan_count}
        for member in top_members
    ]
    return JsonResponse(result, safe=False)


# Number of books in each category
def BooksPerCategory(request):
    categories = Category.objects.annotate(book_count=Count("book"))
    result = [
        {"category": category.category, "book_count": category.book_count}
        for category in categories
    ]
    return JsonResponse(result, safe=False)
