from django.shortcuts import render
from .models import Trainer, Contacts, GymGallery

def home(request):
    trainers = Trainer.objects.all()[:10]
    contacts = Contacts.objects.all()[:2]
    gym_gallery = GymGallery.objects.all()[:10]
    return render(request, 'main/home.html', context={'trainers': trainers, 
                                                      'contacts': contacts, 
                                                      'gym_gallery': gym_gallery,
                                                      })
