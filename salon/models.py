from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class DescriereServicii(models.Model):
    nume = models.CharField(max_length=200, verbose_name="Numele Serviciului")
    descriere = HTMLField(verbose_name="Descriere")
    durata = models.DurationField(verbose_name="Durata")
    pret = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preț")
    imagine = models.ImageField(upload_to='services_images/', verbose_name="Imagine", blank=True, null=True)
    categorie = models.CharField(max_length=100, verbose_name="Categorie")
    available = models.BooleanField(default=True, verbose_name="Disponibil")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Data Adăugării")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualizare")
    promotion = models.TextField(blank=True, null=True, verbose_name="Promoții sau Reduceri")
    # content = HTMLField( ) 

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name_plural = "Descrieri Servicii"


class Programare(models.Model):
    nume = models.CharField(max_length=100, verbose_name="Nume", null=True)
    prenume = models.CharField(max_length=100, verbose_name="Prenume", null=True)
    telefon = models.CharField(max_length=15, verbose_name="Număr de Telefon", null=True)
    email = models.EmailField(verbose_name="Email", null=True)
    serviciu = models.ForeignKey('DescriereServicii', on_delete=models.CASCADE, verbose_name="Serviciu")
    data = models.DateField(verbose_name="Data")
    ora = models.TimeField(verbose_name="Ora")
    confirmat = models.BooleanField(default=False)
    content = HTMLField()  # Presupun că folosești o bibliotecă cum ar fi django-tinymce pentru HTMLField

    def __str__(self):
        return f"{self.nume} {self.prenume} - {self.data.strftime('%Y-%m-%d')} {self.ora}"

    class Meta:
        verbose_name_plural = "Programări"
    

