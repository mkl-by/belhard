from django.urls import path, re_path

from hotels import views

urlpatterns = [
    # path('', views.room_show),
    path('', views.hotels_show, name='hotels_show'),
    # path('booking/<number>/', views.room_booking, name='room-booking')
    # re_path(r'^(?P<number_of_seats>\d)/$', views.Room_show.as_view(), name='room_feature'),
]
