from django.shortcuts import render
from .models import Author, Book, Category
from django.http import JsonResponse
import json
from django.db.models import Count, Q
from django.views.decorators.csrf import csrf_exempt

### Author Endpoints


# GET Returns all authors
def get_authors(request):
    authors = Author.objects.all()

    data = []

    for author in authors:
        data.append(
            {
                "id": author.id,
                "name": author.name,
                "bio": author.bio,
                "date_of_birth": author.date_of_bith,
            }
        )
    # safe=False allows returning a list
    return JsonResponse(data, safe=False)


# GET Returns a single author
def get_author(request, id):
    try:
        author = Author.objects.get(id=id)
        data = {
            "id": author.id,
            "name": author.name,
            "bio": author.bio,
            "date_of_birth": author.date_of_bith,
        }
        return JsonResponse(data)
    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)


# POST create Author
@csrf_exempt
def create_author(request):
    if request.method == "POST":
        body = json.loads(request.body)

        author = Author.objects.create(
            name=body.get("name"),
            bio=body.get("bio"),
            date_of_birth=body.get("date_of_birth"),
        )
        return JsonResponse({"message": "Author created", "id": author.id})


# PUT update author
@csrf_exempt
def update_author(request, id):
    if request.method == "PUT":
        body = json.loads(request.body)

        try:
            author = Author.objects.get(id=id)

            author.name = body.get("name", author.name)
            author.bio = body.get("bio", author.bio)
            author.date_of_bith = body.get("date_of_birth", author.date_of_bith)

            author.save()
            return JsonResponse({"Message": "Author Sucessfuly updated"})

        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)


# DELETE author
@csrf_exempt
def delete_author(request, id):
    if request.method == "DELETE":

        try:
            author = Author.objects.get(id=id)
            author.delete()

            return JsonResponse({"Message": "Author successfuly deleted"})

        except Author.DoesNotExist:
            return JsonResponse({"error": "Author doesn't exist"}, status=404)


# GET all books written by that author
def get_author_books(request, id):
    try:
        author = Author.objects.get(id=id)

        books = Book.objects.filter(author=author)

        data = []
        for book in books:
            data.append(
                {
                    "id": book.id,
                    "title": book.title,
                }
            )
        return JsonResponse(data, safe=False)
    except Author.DoesNotExist:
        return JsonResponse({"error": "Author not found"}, status=404)


# GET the amount of books an author write
def get_author_book_count(request):
    authors = Author.objects.annotate(total_books=Count("book"))

    data = []
    for author in authors:
        data.append({"name": author.name, "total_books": author.total_books})
    return JsonResponse(data, safe=False)


### Book Endpoints


# GET all books
def get_books(request):
    books = Book.objects.all()

    data = []
    for book in books:
        categories = [category.c_name for category in book.categories.all()]
        data.append(
            {
                "Title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "price": str(book.price),
                "available": book.available,
                "Category": categories,
            }
        )
    return JsonResponse(data, safe=False)


# GET book by id
def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
        categories = [c.name for c in book.categories.all()]
        data = {
            "id": book.id,
            "Title": book.title,
            "author": book.author,
            "published_date": book.published_date,
            "isbn": book.isbn,
            "categories": book.categories,
            "price": str(book.price),
            "availble": book.available,
        }
        return JsonResponse(data)

    except Book.DoesNotExist:
        return JsonResponse({"Message": "The book doesn't exist"}, status=404)


# POST create a new book
@csrf_exempt
def create_book(request):
    if request.method == "POST":
        # convert JSON to python dict
        body = json.loads(request.body)

        try:
            # we should fetch the author object because ForeignKey requeiers object not just id
            author = Author.objects.get(id=body.get("author_id"))

            book = Book.objects.create(
                title=body.get("title"),
                author=author,
                published_date=body.get("published_date"),
                isbn=body.get("isbn"),
                price=body.get("price"),
                available=body.get("available", True),
            )
            category_ids = (body.get("category_ids", []),)

            book.catagories.set(category_ids)

            return JsonResponse({"message": "Book created", "id": book.id})

        except Author.DoesNotExist:
            return JsonResponse({"error": "Author not found"}, status=404)


# PUT update a book
@csrf_exempt
def update_book(request, id):
    if request.method == "PUT":
        body = json.loads(request.body)

        try:
            book = Book.objects.get(id=id)

            book.title = (body.get("title", book.title),)
            book.published_date = (body.get("published_date", book.published_date),)
            book.isbn = (body.get("isbn", book.isbn),)
            book.price = (body.get("price", book.price),)
            book.available = body.get("available", book.available)

            # update author - foreign key
            if "author_id" in body:
                book.author = Author.objects.get(id=body.get("author_id"))

            # update category - many to many relationship
            if "category_ids" in body:
                categories = Category.objects.filter(id__in=body.get("category_ids"))
                book.categories.set(categories)

            book.save()
            return JsonResponse({"Message": "book successfully updated"})

        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)


# DELETE book
@csrf_exempt
def delete_book(request, id):
    if request.method == "DELETE":
        try:
            book = Book.objects.get(id=id)
            book.delete()

            return JsonResponse({"message": "Book successfully deleted"})

        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)


### Category endpoints


# GET categories
def get_categories(request):
    categories = Category.objects.all()

    data = []
    for c in categories:
        data.append({"id": c.id, "name": c.c_name})

    return JsonResponse(data, safe=False)


# GET category by id
def get_category(request, id):
    try:
        category = Category.objects.get(id=id)
        data = {"id": category.id, "name": category.c_name}
        return JsonResponse(data)

    except Category.DoesNotExist:
        return JsonResponse({"error": "Category doesn't exist"}, status=404)


# POST create category
@csrf_exempt
def create_category(request):
    if request.method == "POST":

        body = json.loads(request.body)
        try:
            category = Category.objects.create(c_name=body.get("c_name"))
            return JsonResponse(
                {"message": "category successfully created", "id": category.id}
            )

        except Category.DoesNotExist:
            return JsonResponse({"error": "category doesn't exist"}, status=404)


# PUT update category
@csrf_exempt
def update_category(request, id):
    if request.method == "PUT":
        body = json.loads(request.body)

        try:
            category = Category.objects.get(id=id)

            category.c_name = body.get("c_name", category.c_name)

            category.save()
            return JsonResponse({"message": "category sucessfully updated"})

        except Category.DoesNotExist:
            return JsonResponse({"error": "category doesn't exist"})


# DELETE category
@csrf_exempt
def delete_category(request, id):
    if request.method == "DELETE":
        try:
            category = Category.objects.get(id=id)
            category.delete()

            return JsonResponse({"message": "Category successfully deleted"})

        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)


# GET all books under a category
def get_category_books(request, id):
    try:
        category = Category.objects.get(id=id)

        books = Book.objects.filter(categories=category)
        data = []
        for book in books:
            data.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author.name,
                    "available": book.available,
                }
            )
        return JsonResponse(data, safe=False)

    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=404)


### Filtering and Functional endpoints


# GET books by specific author
def get_book_by_author(request, author_id):
    try:
        books = (
            Book.objects.select_related("author")
            .prefetch_related("categories")
            .filter(author_id=author_id)
        )
        data = []
        for book in books:
            data.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author.name,
                    "price": str(book.price),
                    "available": book.available,
                }
            )
        return JsonResponse(data, safe=False)

    except Exception:
        return JsonResponse({"error": "something went wrong"}, status=404)


# GET books by specific category
def get_book_by_category(request, category_id):
    try:
        books = (
            Book.objects.select_related("author")
            .prefetch_related("categories")
            .filter(category_id=category_id)
        )
        data = []
        for book in books:
            data.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author.name,
                    "price": str(book.price),
                    "available": book.available,
                }
            )
        return JsonResponse(data, safe=False)

    except Exception:
        return JsonResponse({"error": "something went wrong"}, status=404)


# GET search books by title
def search_book_title(request):
    query = request.GET.get("q")

    books = (
        Book.objects.select_related("author")
        .prefetch_related("categories")
        .filter(title__icontains=query)
    )
    for book in books:
        data = [
            {
                "id": book.id,
                "title": book.title,
            }
        ]
    return JsonResponse(data, safe=False, status=200)


# GET filter books with price
def filter_price(request):
    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    books = (
        Book.objects.select_related("author")
        .prefetch_related("categories")
        .filter(query=min_price, query=max_price)
    )

    data = [
        {"id": book.id, "title": book.title, "price": str(book.price)} for book in books
    ]
    return JsonResponse(data, safe=False, status=200)


# GET available books
def available_books(request):
    books = (
        Book.objects.select_for_update("author")
        .prefetch_related("categories")
        .filter(available=True)
    )

    data = [
        {"id": book.id, "title": book.title, "price": str(book.price)} for book in books
    ]
    return JsonResponse(data, safe=False, status=200)


# GET order books by published_date
def order_published_date(request):
    books = (
        Book.objects.select_for_update("author")
        .prefetch_related("categories")
        .order_by("published_date")
    )

    data = [
        {"id": book.id, "title": book.title, "price": str(book.price)} for book in books
    ]
