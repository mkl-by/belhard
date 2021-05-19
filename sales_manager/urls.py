from django.contrib import admin
from django.urls import path, include

from sales_manager import views

urlpatterns = [
      path('book_datail/<int:book_id>', views.book_datail, name='book_datail'),
      path('', views.main_page),

]