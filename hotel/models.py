from django.db import models

# Create your models here.
class Room(models.Model):

    number_room = models.IntegerField(unique=True)

class Room_feature(models.Model):
    # Характеристики номера
    num_of_seats = ((1, 'одноместный'), (2, 'двухместный'), (3, 'трехместный'), ('L', 'Люкс'))

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_of_seats = models.CharField(max_length=1, choices=num_of_seats)
    occupation = models.BooleanField(default=False)
    removed = models.BooleanField(default=True)

    def __str__(self):
        return self.room
