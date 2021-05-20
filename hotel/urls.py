from django.urls import path, re_path

from hotel import views

urlpatterns = [
    path('', views.room_show),
    re_path(r'^hotel/(?P<room_id>\d+)/$', views.room_feature, name='room_feature'),
]
