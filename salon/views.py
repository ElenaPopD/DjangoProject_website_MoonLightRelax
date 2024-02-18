from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse  # noqa: F401
from .models import  DescriereServicii
from django.db.models import F 
from .forms import ProgramareForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def servicii(request):
    servicii = DescriereServicii.objects.all()
    return render(request, 'servicii.html', {'servicii': servicii})


def programare(request):
    if request.method == 'POST':
        form = ProgramareForm(request.POST)
        if form.is_valid():
            form.save()
            send_confirmation_email(form.instance, 'Programare înregistrată', 'Programare înregistrată cu succes! Vei primi un email de confirmare în cel mai scurt timp posibil!')
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
    return HttpResponse('Email trimis cu succes!')  # noqa: F841