from django.contrib import admin
from .models import Booking, BookingMedia, BookingNumbers

admin.site.register(Booking)
admin.site.register(BookingNumbers)
admin.site.register(BookingMedia)
