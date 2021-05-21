from django.shortcuts import render, HttpResponse
from .models import Room_feature, Room

# Create your views here.
def room_show(request):
    #room = Room.objects.all()
    room = Room.objects.filter(pk__in=list(map(lambda x: x['room_id'],
                                               Room_feature.objects.all().values('room_id'))))

    context = {'name': room }
    return render(request, 'hotel/room.html', context)

def room_feature(request, room_id):

    roomid = int(room_id)
    try:
        feature = Room_feature.objects.get(room_id=roomid)
    except:
        return HttpResponse("<html><body><h1>Помещение сгорело</h1></body></html>")

    number = Room.objects.get(id=room_id)
    contex = {'feature': feature, 'number': number}
    return render(request, 'hotel/room_feature.html', contex)
