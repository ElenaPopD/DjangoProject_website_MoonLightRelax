from django.contrib import admin
from .models import Programare, DescriereServicii, Despre, ContactInfo
from .views import send_confirmation_email
# Register your models here.

class ProgramareAdmin(admin.ModelAdmin):
    list_display = ('nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'confirmat')
    list_filter = ('data', 'confirmat')
    search_fields = ('nume', 'prenume', 'telefon', 'email', 'serviciu', 'data', 'ora', 'confirmat')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Verifică dacă 'confirmat' a fost modificat
        if 'confirmat' in form.changed_data:
            if obj.confirmat:
                # Trimitere email de confirmare
                body_email = f"""\
Dragă {obj.prenume} {obj.nume},

Suntem încântați să-ți confirmăm rezervarea la Moonlight Relax pentru serviciul de {obj.serviciu}. Detaliile tale de programare sunt pentru data de {obj.data.strftime('%d-%m-%Y')}, ora {obj.ora.strftime('%H:%M')}.

Așteptăm cu nerăbdare să te întâmpinăm în oază noastră de relaxare și să îți oferim o experiență de neuitat.

Cu drag,
Echipa Moonlight Relax
"""
                titu_email = 'Confirmarea Rezervării Tale la Moonlight Relax'
                send_confirmation_email(obj, titu_email, body_email)
            else:
                # Trimitere email de anulare
                body_email = f"""\
Dragă {obj.prenume} {obj.nume},

Ne pare rău să te informăm că rezervarea ta pentru {obj.serviciu} programată pentru data de {obj.data.strftime('%d-%m-%Y')}, ora {obj.ora.strftime('%H:%M')}, a trebuit să fie anulată.

Înțelegem cât de importantă este pentru tine această experiență și îți cerem scuze pentru orice inconveniență. Te rugăm să ne contactezi pentru a reprograma sau pentru orice alte întrebări pe care le ai.

Îți mulțumim pentru înțelegere și sperăm să te putem întâmpina în curând la Moonlight Relax.

Cu considerație,
Echipa Moonlight Relax
"""
                titu_email = 'Anularea Rezervării Tale la Moonlight Relax'
                send_confirmation_email(obj, titu_email, body_email)

admin.site.register(Programare, ProgramareAdmin)

class DescriereServiciiAdmin(admin.ModelAdmin):
    list_display = ('nume', 'descriere', 'durata', 'pret', 'categorie', 'available', 'added_on', 'last_updated', 'promotion')
    list_filter = ('categorie', 'available', 'added_on', 'last_updated')
    search_fields = ('nume', 'descriere', 'durata', 'pret', 'categorie', 'available', 'added_on', 'last_updated', 'promotion')

admin.site.register(DescriereServicii, DescriereServiciiAdmin)

class DespreAdmin(admin.ModelAdmin):
    nume = "Despre"
    list_display = ('nume', 'imagine', 'descriere', 'added_on', 'last_updated')
    list_filter = ('added_on', 'last_updated')
    search_fields = ('nume', 'imagine', 'descriere', 'added_on', 'last_updated')



admin.site.register(Despre, DespreAdmin)
admin.site.register(ContactInfo)



