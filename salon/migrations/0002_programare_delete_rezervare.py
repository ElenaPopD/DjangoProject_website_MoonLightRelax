# Generated by Django 5.0.1 on 2024-02-18 10:12

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100, null=True, verbose_name='Nume')),
                ('prenume', models.CharField(max_length=100, null=True, verbose_name='Prenume')),
                ('telefon', models.CharField(max_length=15, null=True, verbose_name='Număr de Telefon')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('data', models.DateField(verbose_name='Data')),
                ('ora', models.TimeField(verbose_name='Ora')),
                ('confirmat', models.BooleanField(default=False)),
                ('content', tinymce.models.HTMLField()),
                ('serviciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.descriereservicii', verbose_name='Serviciu')),
            ],
            options={
                'verbose_name_plural': 'Programări',
            },
        ),
        migrations.DeleteModel(
            name='Rezervare',
        ),
    ]
