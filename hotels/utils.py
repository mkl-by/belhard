from django.core.exceptions import ValidationError
from PIL import Image
from django.db.models import Q
from django.forms import models

from hotels.models import Booking

def dataofentry(start_date, end_date):
    return Booking.objects.exclude(
        Q(date_start__gte=start_date, date_end__lte=end_date) |
        Q(date_start__lte=start_date, date_end__gte=end_date) |
        Q(date_start__gte=start_date, date_start__lte=end_date, date_end__gte=end_date) |
        Q(date_end__gte=start_date, date_end__lte=end_date, date_start__lte=end_date)
    )
