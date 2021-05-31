from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.decorators.http import require_http_methods
from datetime import date
from .models import Room_feature, Room, Rating

# Create your views here.
def pars_data(data):
    dt = data.split('-')
    return (date(int(dt[0]), int(dt[1]),int(dt[2])))

class Room_show(View):
    def get(self, request):
        return render(request, 'hotel/room.html')

    def post(self, request):
        seats = request.POST['room_of_seats']
        datastart = pars_data(request.POST['datastart'])
        dataend = pars_data(request.POST['dataend'])
        print((datastart < dataend))
        if ((0 < int(seats) <= 3) & (datastart < dataend)):
            room = Room_feature.objects.filter(
                room__number_of_seats=seats,
                booking_data_start__gt=datastart,
                booking_data_end=dataend
            )

            return render(request, 'hotel/room.html', {'room': room, 'number_of_seats': seats})
        return redirect('room_feature')


@require_http_methods(['POST'])
def room_booking(request, number):
    text = request.POST['text']
    datastart = pars_data(request.POST['datastart'])
    dataend = pars_data(request.POST['dataend'])

    if datastart < dataend:
        room = Room.objects.get(number_room=number)
        Room_feature.objects.create(
            bookaroom=request.user,
            occupation_description=text,
            room=room,
            booking_data_start=datastart,
            booking_data_end=dataend,
            )
        return redirect('room_feature')
    return redirect('room_feature')


