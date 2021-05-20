from django.shortcuts import render, HttpResponse
from .models import Room_feature, Room

# Create your views here.
def room_show(request):
    room = Room.objects.all()
    context = {'name': room }
    return render(request, 'hotel/room.html', context)

def room_feature(request, room_id):

    room_id = int(room_id)


    feature = Room_feature.objects.get(room_id=room_id)
    number = Room.objects.get(id=room_id)


    contex = {'feature': feature, 'number': number}
    return render(request, 'hotel/room_feature.html', contex)
