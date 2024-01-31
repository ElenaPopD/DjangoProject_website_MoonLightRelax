from django.shortcuts import render
from django.http import HttpResponse
from .models import  DescriereServicii, Rezervare
from django.db.models import F 

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def servicii(request):
    servicii = DescriereServicii.objects.all()
    return render(request, 'servicii.html', {'servicii': servicii})

def contact(request):
    return render(request, 'contact.html')

def rezervari(request):
    rezervari = Rezervare.objects.all()

    return render(request, 'rezervari.html', {'rezervari': rezervari})