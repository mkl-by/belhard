from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import Room_feature, Room, Rating

# Create your views here.
class Room_show(View):
    def get(self, request):
        return render(request, 'hotel/room.html')

    def post(self, request):
        seats = request.POST['room_of_seats']

        if 0 < int(seats) <= 3:
            room = Room.objects.filter(number_of_seats=seats)
            return render(request, 'hotel/room.html', {'room': room})
        return redirect('room_feature')

class Room_booking(View):
    pass
