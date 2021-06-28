from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField
from hotels.models import Hotels, Room, Booking
from django.db.models import Q
import datetime


class HotelsListserializer(ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['id', 'name', 'city', 'star', 'picture']
        # fields = "__all__"

class HotelCreateSerialiser(ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['name', 'city', 'picture']

class RoomListserializer(ModelSerializer):
    # достаем все записи
    hotel = HotelsListserializer()
    # достаем только одну запись
    hotel_name = serializers.ReadOnlyField(source='hotel.name', read_only=True)
    class Meta:
        model = Room
        # read_only_field=('city', 'star')
        # fields = "__all__"
        fields = ['id', 'description', 'numberofseats', 'imgroom', 'hotel_id', 'hotel_name', 'hotel']

class BookingListSerializer(ModelSerializer):
    room = RoomListserializer()
    #username = CharField(source='user.username')
    class Meta:
        model = Booking
        fields = ['user', 'room', 'date_start', 'date_end']


class BookinglSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = ['user', 'room', 'date_start', 'date_end']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError("finish must occur after start")
        """
        Checking for employment during this period 
        """
        #
        # if consilience:
        #     raise serializers.ValidationError(f"Дата с {data['date_start'].strftime('%Y-%m-%d')} по {data['date_end']} не может быть выбрана")

        return data
