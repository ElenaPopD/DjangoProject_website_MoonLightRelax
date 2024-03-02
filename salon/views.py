from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse  # noqa: F401
from django.contrib import messages  # Adaugă această linie
from .models import DescriereServicii
from .forms import ProgramareForm
from .models import Despre



def homepage(request):
    context = {'is_homepage': True}
    return render(request, 'homepage.html', context)

def servicii(request):
    servicii = DescriereServicii.objects.all()
    return render(request, 'servicii.html', {'servicii': servicii})

def programare(request):
    if request.method == 'POST':
        form = ProgramareForm(request.POST)
        if form.is_valid():
            form.save()
            subiect_email = "🌙 Programare înregistrată la MoonlightRelax salon"
            mesaj_email = """\
Felicitări! Rezervarea ta la salonul Moonlight Relax a fost înregistrată cu succes.

Ne bucurăm să te avem oaspete și suntem pregătiți să îți oferim o experiență de neuitat, plină de relaxare și reînnoire.

Vei primi în curând un email de confirmare cu toate detaliile necesare. Te rugăm să verifici și folderul de spam, pentru a te asigura că primești toate informațiile importante.

Îți mulțumim pentru încrederea acordată și abia așteptăm să te întâmpinăm în sanctuarul nostru de relaxare.

Cu drag,
Echipa Moonlight Relax
"""
            send_confirmation_email(form.instance, subiect_email, mesaj_email)
            # Adaugă un mesaj care să fie afișat utilizatorului
            messages.success(request, 'Rezervarea a fost înregistrată cu succes. Verifică adresa de email pentru confirmare.')
            return redirect('programare')
    else:
        form = ProgramareForm() 
    return render(request, 'programare.html', {'form': form})

def send_confirmation_email(programare, subiect_email, mesaj_email):
    print(programare)
    subject = subiect_email
    message = mesaj_email
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [programare.email, ]
    send_mail(subject, message, email_from, recipient_list)



def about(request):
    informatii = Despre.objects.all()
    return render(request, 'about.html', {'informatii': informatii})


