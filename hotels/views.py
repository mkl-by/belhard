import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, CreateView
from django.views.generic.base import View
from django.db.models import Q, Avg
from rest_framework import status, serializers, renderers
from rest_framework.response import Response
from rest_framework.views import APIView

from hotels import utils
from hotels.forms import RegistrationForm, LoginUserForm
from hotels.models import Hotels, TypeService, UserTypeService, Room, Booking

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, GenericAPIView, get_object_or_404
from hotels.serializers import HotelsListserializer, RoomListserializer, BookingListSerializer, BookinglSerializer, \
    HotelCreateSerialiser
from django_filters import rest_framework as filters
from rest_framework import filters

def hotels_show(request):
    all_hotels = Hotels.objects.filter(works=True).order_by('name')
    return render(request, 'hotels/index.html', {'hotels': all_hotels})

class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'hotels/registration.html'
    success_url = reverse_lazy('login')

class LoginUser(View):
    def get(self, request):
        return render(request, 'hotels/loginuser.html')
    def post(self, request):
        user = authenticate(
            username=request.POST['login'],
            password=request.POST['psw'])
        if user is not None:
            login(request, user)
            return redirect('hotels_show')
        else:
            return redirect('loginuser')

def logout_view(request):
    logout(request)
    return redirect('hotels_show')

def ServiseSave(request, hotel_id, type_id, rate=3):
    UserTypeService.objects.update_or_create(
        user_id=request.user.id,
        type_service_id=type_id,
        defaults={'rate': rate}
    )
    ts = TypeService.objects.get(id=type_id)
    ts.avg_rate = ts.rated_type_service.aggregate(rate=Avg("rate"))['rate']
    ts.hotel_id = hotel_id
    ts.save(update_fields=['avg_rate', 'hotel_id'])


class Raiting(View):

    def get(self, request, hotel_id, name_hotel):
        if request.user.is_authenticated:
            datanow = datetime.now().date()
            booking = utils.dataofentry(datanow, datanow)


            rooms = Room.objects.filter(hotel=hotel_id).order_by('numberofseats')
            seat = rooms.values('numberofseats').distinct() #выбираем уникальные значения из поля

            try:
                rooms = rooms.filter(numberofseats=request.GET['optradio'])
            except MultiValueDictKeyError:
                pass

            rat = TypeService.objects.all()
            rate = rat.filter(hotel_id=hotel_id)
            if not rate:
                title = rat.values('id')
                for i in title:
                    ServiseSave(request, hotel_id, i['id'])
                rate = TypeService.objects.filter(hotel_id=hotel_id)

            return render(request, 'hotels/rating.html', {'rate': rate,
                                                          'name': name_hotel,
                                                          'hotel_id': hotel_id,
                                                          "rooms": rooms,
                                                          'seat': seat
                                                          })
        return redirect('loginuser')


    def post(self, request):
        if request.user.is_authenticated:
            type_id = request.POST['tipe_id']
            ratki = request.POST['ratk']
            hotel_id = request.POST['hotel_id']
            rat_title = request.POST['name_hotel']
            ServiseSave(request, hotel_id, type_id, ratki)
            rate = TypeService.objects.filter(hotel_id=hotel_id, title=rat_title).first()
            return HttpResponse(rate.avg_rate)
            # return render(request, 'hotels/rating.html', {'rate': rate, 'name': name_hotel, 'hotel_id': hotel_id})
        return redirect('loginuser')

class HotelCreateAPIView(CreateAPIView):
    serializer_class = HotelCreateSerialiser


class HotelsListApiView(ListAPIView):
    queryset = Hotels.objects.all().order_by('name')
    serializer_class = HotelsListserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['city', 'star']
    #renderer_classes = [renderers.JSONRenderer] #ОТКЛЮЧАЕТ production browsable api ТОЛЬКО В ЭТОЙ ВЬЮХЕ
    # точное совпадение
    # filter_backends = (filters.DjangoFilterBackend,)
# filterset_fields = ('city', 'star')
    # по нескольким знакам совпадение


class RoomsListApiView(APIView):
#     booked_rooms = Booking.objects.filter(
#         Q(date_start__gte=start_date, date_end__lte=end_date) |
#         Q(date_start__lte=start_date, date_end__gte=end_date) |
#         Q(date_start__gte=start_date, date_start__lte=end_date, date_end__gte=end_date) |
#         Q(date_end__gte=start_date, date_end__lte=end_date, date_start__lte=end_date)
#     )
#
    def get(self, request, hotel_id):
        query_set = Room.objects.filter(hotel=hotel_id).related_select_related('hotel')
        serializer = RoomListserializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookingListApiView(APIView):
    #renderer_classes = [renderers.JSONRenderer]

    def get(self, request, hotel_id):
        date_now = datetime.date.today()
        #выбираем комнату из отеля по его id, и на сегодняшний момент не занятую
        query_set = Booking.objects.filter(room__hotel=hotel_id).\
            exclude(date_start__lte=date_now, date_end__gte=date_now).\
            select_related('room')

        serializer = BookingListSerializer(query_set, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, hotel_id):

        serializer = BookinglSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            date_start = datetime.datetime.strptime(serializer.data['date_start'], '%Y-%m-%d')
            print(date_start)
            date_end = datetime.datetime.strptime(serializer.data['date_end'], '%Y-%m-%d')
            romm = get_object_or_404(Room, id=serializer.data['room'])
            consilience = Booking.objects.filter(room=romm). \
                filter(Q(date_start__gte=date_start, date_end__lte=date_end) |
                   Q(date_start__lte=date_start, date_end__gte=date_end) |
                   Q(date_start__gte=date_start, date_start__lte=date_end, date_end__gte=date_end) |
                   Q(date_end__gte=date_start, date_end__lte=date_end, date_start__lte=date_end)).exists()
            if consilience:
                raise serializers.ValidationError(f"Дата с {serializer.data['date_start']} по {serializer.data['date_end']} не может быть выбрана")
            serializer.save()
        # пока бронь не пишем, не забудь сделать запись в базу
        # {"user": 1, "room": 13, "date_start": "2021-06-25", "date_end": "2021-06-30"}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





