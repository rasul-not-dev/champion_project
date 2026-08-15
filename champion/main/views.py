from django.shortcuts import render
from .models import Trainer, Contacts, GymGallery

def home(request):
    trainers = Trainer.objects.all()
    contacts = Contacts.objects.all()[:2]
    gym_gallery = GymGallery.objects.all()
    return render(request, 'main/home.html', context={'trainers': trainers, 
                                                      'contacts': contacts, 
                                                      'gym_gallery': gym_gallery
                                                      
                                                      })
