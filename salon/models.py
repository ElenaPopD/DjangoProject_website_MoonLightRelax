from django.db import models
from tinymce.models import HTMLField
from django.core.validators import RegexValidator

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
    promotion = HTMLField(verbose_name="Promoții", blank=True, null=True, default="")
    

    def __str__(self):
        return self.nume

    class Meta:
        verbose_name_plural = "Descrieri Servicii"


class Programare(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Numărul de telefon trebuie să contina doar cifre în formatul: '000 000 000'. Permise până la 15 cifre.")
    nume = models.CharField(max_length=100, verbose_name="Nume", null=True)
    prenume = models.CharField(max_length=100, verbose_name="Prenume", null=True)
    telefon = models.CharField(validators=[phone_regex], max_length=15, verbose_name="Număr de Telefon", null=True)  # Adăugăm validatorul aici
    email = models.EmailField(verbose_name="Email", null=True)
    serviciu = models.ForeignKey('DescriereServicii', on_delete=models.CASCADE, verbose_name="Serviciu")
    data = models.DateField(verbose_name="Data")
    ora = models.TimeField(verbose_name="Ora")
    confirmat = models.BooleanField(default=False)
    observatii = HTMLField(verbose_name="Observații", null=True, blank=True)

    def __str__(self):
        return f"{self.nume} {self.prenume} - {self.data.strftime('%Y-%m-%d')} {self.ora}"

    class Meta:
        verbose_name_plural = "Programări"
    


class Despre(models.Model):
    nume = models.CharField(max_length=100, verbose_name="Nume", default="Despre")
    imagine = models.ImageField(upload_to='about_images/', verbose_name="Imagine", blank=True, null=True)
    descriere = HTMLField(verbose_name="Descriere")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Data Adăugării")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualizare")

    def __str__(self):
        return "Despre"
        

    class Meta:
        verbose_name_plural = "Despre"

class ContactInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nume", default="Informații de contact")
    content = HTMLField(verbose_name="Conținut")
    email = models.EmailField(max_length=255, verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Număr de Telefon")
    facebook_page = models.URLField(max_length=255, verbose_name="Pagina de Facebook")
    instagram = models.URLField(max_length=255,  verbose_name="Pagina de Instagram")
    address = models.TextField(verbose_name="Adresa Salonului")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Data Adăugării")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualizare")
    

    def __str__(self):
        return "Informații de contact"
    
    class Meta:
        verbose_name_plural = "Informații de contact"

class Politica_Confidentialitate(models.Model):
    nume = models.CharField(max_length=100, verbose_name="Nume", default="Politica de Confidențialitate")
    continut = HTMLField(verbose_name="Conținut")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Data Adăugării")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualizare")

    def __str__(self):
        return "Politica de Confidențialitate"
    
    class Meta:
        verbose_name_plural = "Politica de Confidențialitate"

class Termeni_si_conditii(models.Model):
    nume = models.CharField(max_length=100, verbose_name="Nume", default="Termeni și Condiții")
    continut = HTMLField(verbose_name="Conținut")
    added_on = models.DateTimeField(auto_now_add=True, verbose_name="Data Adăugării")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Ultima Actualizare")

    def __str__(self):
        return "Termeni și Condiții"
    
    class Meta:
        verbose_name_plural = "Termeni și Condiții"