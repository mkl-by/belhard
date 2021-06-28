from django.contrib import admin

# Register your models here.
from hotels.models import Hotels, TypeService, UserTypeService, Room, Booking


class AdminBd(admin.ModelAdmin):
    list_display = ('name', 'city', 'star', 'works', 'picture', 'picture_smal')




admin.site.register(Hotels)
admin.site.register(TypeService)
admin.site.register(UserTypeService)
admin.site.register(Room)
admin.site.register(Booking)
