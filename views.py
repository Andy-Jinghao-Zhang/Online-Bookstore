from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book


def home(request):
    query = request.GET.get("search", "").strip()
    books = Book.objects.all().order_by("title")

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, "store/home.html", {
        "books": books,
        "query": query,
    })


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    return render(request, "store/book_detail.html", {
        "book": book,
    })
