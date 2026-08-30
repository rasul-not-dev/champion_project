from django.shortcuts import render
from .models import Price

def payment(request):
    price_and_qr = Price.objects.first()
    return render(request, 'payment/payment.html', context={'price_and_qr': price_and_qr})
