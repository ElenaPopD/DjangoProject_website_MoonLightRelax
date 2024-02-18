from django.contrib import admin
from .models import Programare, DescriereServicii
from .views import send_confirmation_email
# Register your models here.

class ProgramareAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'confirmat')
    list_filter = ('data', 'confirmat')
    search_fields = ('nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'confirmat')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Verifică dacă 'confirmat' a fost setat pe True și trimite e-mailul de confirmare
        if 'confirmat' in form.changed_data and obj.confirmat:
            body_email = f"Bună, {obj.prenume} {obj.nume} \n\nRezervarea ta pentru {obj.serviciu} a fost confirmată cu succes pentru data de {obj.data}, de la ora {obj.ora}! \n\nNe vedem curând,\nMoonlight Relax"
            titu_email = 'Confirmare Rezervare Moonlight Relax'
            send_confirmation_email(obj, titu_email, body_email)


admin.site.register(Programare, ProgramareAdmin)


class DescriereServiciiAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere', 'durata', 'pret', 'categorie', 'available', 'added_on', 'last_updated', 'promotion')
    list_filter = ('categorie', 'available', 'added_on', 'last_updated')
    search_fields = ('nume', 'descriere', 'durata', 'pret', 'categorie', 'available', 'added_on', 'last_updated', 'promotion')


admin.site.register(DescriereServicii, DescriereServiciiAdmin)