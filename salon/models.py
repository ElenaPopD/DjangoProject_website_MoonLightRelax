from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class DescriereServicii(models.Model):
    nume = models.CharField(max_length=200, verbose_name="Numele Serviciului")
    pret = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preț")
    durata = models.DurationField(verbose_name="Durata")
    descriere = HTMLField(verbose_name="Descriere")
    imagine = models.ImageField(upload_to='services_images/', verbose_name="Imagine", blank=True, null=True)
    categorie = models.CharField(max_length=100, verbose_name="Categorie")
    available = models.BooleanField(default=True, verbose_name="Disponibil")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Data Adăugării")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualizare")
    promotion = models.TextField(blank=True, null=True, verbose_name="Promoții sau Reduceri")

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name_plural = "Descrieri Servicii"


class Rezervare(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=15)
    serviciu = models.CharField(max_length=100)
    data = models.DateField()
    ora = models.TimeField()
    content= HTMLField()

    def __str__(self):
        return f"{self.nume} {self.prenume} - {self.data} {self.ora}"
    

