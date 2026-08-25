from django.shortcuts import render
from .models import Timetable

def timetable(request):
    timetable = Timetable.objects.all()
    return render(request, 'timetable/timetable.html', context={'timetable': timetable})