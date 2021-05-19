from django.shortcuts import render, HttpResponse

# Create your views here.
def main_page(request):
    return render(request, 'sales_manager/index.html')