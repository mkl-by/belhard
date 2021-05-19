from django.shortcuts import render, HttpResponse
from sales_manager.models import Book

# Create your views here.
def main_page(request):
    query_set = Book.objects.all()
    context = {'queryset': query_set}
    return render(request, 'sales_manager/index.html', context)

def book_datail(request, book_id):
    book = Book.objects.get(id=book_id)
    cont = {'book': book}
    return render(request, 'sales_manager/book_datail.html', cont)