import requests
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from PIL import Image


# Create your models here.

class Hotels(models.Model):
    # size = (300, 300)
    name = models.CharField(max_length=70, unique=True) # название отеля
    city = models.CharField(max_length=70)
    star = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    # количество звезд отеля
    works = models.BooleanField(default=True)  # используем в случае если отель будет на ремонте или сгорит, в выборке если тру то показываем
    picture = models.ImageField(upload_to='imageshotel/%Y/%m/%d',
                                verbose_name=' Изображение отеля',
                                blank=True,
                                null=True
                               )
    # ссылки на картинки
    # manager = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_hotels')
    # rating = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='user_hotels')

    # def save(self):
    #     super().save()
    #     image_path = self.picture.path
    #     img = Image.open(image_path)
    #     min_h, min_w = self.size
    #     if img.height < min_h or img.width < min_w:
    #         raise ValidationError('Разрешение изображения меньше минимального')
    #     else:
    #         img.thumbnail(self.size)
    #         img.save(self.picture.path)

    def __str__(self):
        return self.name
# book = models.ForeignKey(Book, on_delete=models.CASCADE, limit_choices_to={'works': True})

class TypeService(models.Model):
    hotel = models.ForeignKey(Hotels, null=True, blank=True, on_delete=models.SET_NULL, related_name='hotelservice')
    title = models.CharField(max_length=50)
    avg_rate = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    user = models.ManyToManyField(
        User,
        related_name="rated_services",
        blank=True
    )

    def __str__(self):
        return self.title

class UserTypeService(models.Model):
    class Meta:
        unique_together = ("user", "type_service")

    user = models.ForeignKey(
        User,
        related_name="rated_type_service",
        on_delete=models.SET_DEFAULT,
        default=3
    )
    type_service = models.ForeignKey(
        TypeService,
        on_delete=models.CASCADE,
        related_name="rated_type_service"
    )
    rate = models.PositiveSmallIntegerField()

class Room(models.Model):
    hotel = models.ForeignKey(Hotels, null=True, on_delete=models.SET_NULL, related_name='hotelroom')
    description = models.CharField(max_length=250, null=True, blank=True)
    # количество мест
    numberofseats = models.PositiveSmallIntegerField(default=1)
    imgroom = models.ImageField(upload_to='imagesroom/%Y/%m/%d',
                                verbose_name=' Изображение комнаты',
                                blank=True,
                                null=True
                               ) # ссылки на картинки
    def __str__(self):
        return str(self.numberofseats)

class Status(models.Model):
    look = models.BooleanField(default=False) # На рассмотрении
    accepted = models.BooleanField(default=False) # принято
    rejected = models.BooleanField(default=False) # отклонено



class Booking(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='bookinguser')
    room = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL, related_name='bookingroom')
    #status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL, related_name='bookingstatus')
    date_start = models.DateField()
    date_end = models.DateField()
    data_booking = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return str(self.data_booking)
