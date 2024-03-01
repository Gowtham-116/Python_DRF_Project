from django.shortcuts import render,get_object_or_404
from book_outlet.models import Book
from django.http import Http404
from django.db.models import Avg,Min

# Create your views here.

def index(request):
    books=Book.objects.all().order_by("-title")
    num_books=books.count()     
    avg_rating=books.aggregate(Avg("ratings"),Min("ratings"))
    return render (request,"book_outlet/index.html",{
        "books":books,
        "totalnumofbooks":num_books,
        "avgrating":avg_rating
    })

def book_detail(request,slug):
    # try:
    #     book=Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    book=get_object_or_404(Book,slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author":book.author,
        "is_bestseller": book.is_bestselling,
        "rating":book.ratings
    })