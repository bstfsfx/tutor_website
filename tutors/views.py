from django.shortcuts import render
from django.views.generic import ListView
from .models import Tutor
# Create your views here.

def tutors(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutors/tutors.html', {'tutors': tutors})

def tutor(request, tutor_id):
    tutor = Tutor.objects.get(id=tutor_id)
    return render(request, 'tutors/tutor.html', {'tutor': tutor})