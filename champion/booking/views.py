from django.shortcuts import render
from .models import Booking, BookingMedia, BookingNumbers

def booking(request):
    booking = Booking.objects.first()
    bookingMedia = BookingMedia.objects.all()
    bookingNumbers = BookingNumbers.objects.all()
    return render(request, 'booking/booking.html', context={'booking': booking, 'bookingMedia': bookingMedia, 'bookingNumbers': bookingNumbers})