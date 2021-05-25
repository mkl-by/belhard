from django.urls import path, re_path

from hotel import views

urlpatterns = [
    # path('', views.room_show),
    path('', views.Room_show.as_view(), name='room_feature'),
    path('booking', views.Room_booking.as_view(), name='room-booking')
    # re_path(r'^(?P<number_of_seats>\d)/$', views.Room_show.as_view(), name='room_feature'),
]
