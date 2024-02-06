from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import  DescriereServicii, Rezervare
from django.db.models import F 
from .forms import ContactForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def servicii(request):
    servicii = DescriereServicii.objects.all()
    return render(request, 'servicii.html', {'servicii': servicii})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subiect = form.cleaned_data["subiect"]
            mesaj = form.cleaned_data["mesaj"]
            email = form.cleaned_data["email"]
            send_mail(subiect, mesaj, from_email="contact@gmail.com", recipient_list=[email])
            return redirect("/")
    return render(request, "contact.html", {"form": form})

def rezervari(request):
    rezervari = Rezervare.objects.all()

    return render(request, 'rezervari.html', {'rezervari': rezervari})