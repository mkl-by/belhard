from django.urls import path, re_path
from django.conf.urls.static import static
from hotel import views
from django.conf import settings

urlpatterns = [
    # path('', views.room_show),
    # path('', views.Room_show.as_view(), name='room_feature'),
    # path('booking/<number>/', views.room_booking, name='room-booking')
    # re_path(r'^(?P<number_of_seats>\d)/$', views.Room_show.as_view(), name='room_feature'),
]


