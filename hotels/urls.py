from django.urls import path, re_path

from hotels import views
from hotels.views import HotelsListApiView, RoomsListApiView, BookingListApiView

urlpatterns = [
    # path('', views.room_show),
    path('', views.hotels_show, name='hotels_show'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('loginuser/', views.LoginUser.as_view(), name='loginuser'),
    path('logout/', views.logout_view, name='logout'),
    path('rating/<int:hotel_id>/<str:name_hotel>/', views.Raiting.as_view(), name='rating'),
    path('rating-ajax/', views.Raiting.as_view()),
    path('api_hotels/', HotelsListApiView.as_view()),
    path('api/room/<int:hotel_id>/', RoomsListApiView.as_view()),
    path('api/<int:hotel_id>/', BookingListApiView.as_view()),
    # path('rating/<int:hotel_id>/<str:name_hotel>/<int:rate>/', views.Raiting1.as_view(), name='ratingone'),

    # path('rating/<int:hotel_id>/<str:name_hotel>/<int:type_id>/<int:rat>/', views.Raiting1.as_view(), name='rating_one'),
    # path('booking/<number>/', views.room_booking, name='room-booking')
    # re_path(r'^(?P<number_of_seats>\d)/$', views.Room_show.as_view(), name='room_feature'),
]
