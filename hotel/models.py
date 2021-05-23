# import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Room(models.Model):
    # Характеристики номера
    number_room = models.CharField(primary_key=True, max_length=30, unique=True)
    number_of_seats = models.PositiveSmallIntegerField(default=0)
    occupation = models.BooleanField(default=False)  # бронирован или нет
    removed = models.BooleanField(default=True)
    feature = models.TextField(null=True, blank=True) # описание комнаты
    def __str__(self):
        return f'Номер комнаты {self.number_room}'

class Rating(models.Model):
    #Оценка за предоставленную услулгу
    val = models.JSONField()
    sum_vall = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Общая оценка за предоставленную услугу {self.sum_vall}"

class Room_feature(models.Model):
    # Бронирование номера
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room') # что забронировал
    bookaroom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookaroom') # кто забронировал, лучше назвать юзером
    rating = models.ManyToManyField(Rating)
    occupation_description = models.TextField(null=True, blank=True) # описание бронирования
    # num_of_seats = (('1', 'одноместный'), ('2', 'двухместный'), ('3', 'трехместный'), ('L', 'Люкс'))
    datapublished = models.DateTimeField(auto_now_add=True, db_index=True)
    booking_data_start = models.DateField()
    booking_data_end = models.DateField()

    def __str__(self):
        return self.room

