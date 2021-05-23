from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from sales_manager.models import Book
from django.views import View
from django.db.models import Count

# Create your views here.
def main_page(request):
    query_set = Book.objects.all().select_related('author').annotate(count_likes=Count('likes'))
    context = {'queryset': query_set}
    return render(request, 'sales_manager/index.html', context)

def book_datail(request, book_id):
    book = Book.objects.get(id=book_id)
    cont = {'book': book}
    return render(request, 'sales_manager/book_datail.html', cont)

@login_required()
def add_like(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user in book.likes.all():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
    return redirect('main_page')

class LoginView(View):
    def get(self, request):
        return render(request, 'sales_manager/loginhtml.html')
    def post(self, request):
        user = authenticate(
            username=request.POST['login'],
            password=request.POST['psw'])
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            return redirect('login')


def logout_view(request):
    logout(request)
    return redirect(main_page)