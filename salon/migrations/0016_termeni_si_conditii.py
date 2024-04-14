# Generated by Django 5.0.3 on 2024-04-14 15:01

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0015_politica_confidentialitate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Termeni_si_conditii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(default='Termeni și Condiții', max_length=100, verbose_name='Nume')),
                ('continut', tinymce.models.HTMLField(verbose_name='Conținut')),
                ('added_on', models.DateTimeField(auto_now_add=True, verbose_name='Data Adăugării')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Ultima Actualizare')),
            ],
            options={
                'verbose_name_plural': 'Termeni și Condiții',
            },
        ),
    ]
