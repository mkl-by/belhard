from django.contrib import admin
from django.urls import path, include

from sales_manager import views

urlpatterns = [
      path('book_datail/<int:book_id>', views.book_datail, name='book_datail'),
      path('', views.main_page, name='main_page'),
      path('book_like/<int:book_id>', views.add_like, name='book_like'),
      path('login/', views.LoginView.as_view(), name='login'),
      path('logout/', views.logout_view, name='logout'),
      path('add_comment/<int:book_id>/', views.add_comment, name='add_comment'),
]
