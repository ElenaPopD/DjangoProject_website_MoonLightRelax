# Generated by Django 5.0.3 on 2024-03-23 19:43

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_despre_nume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programare',
            name='content',
        ),
        migrations.AddField(
            model_name='programare',
            name='observatii',
            field=tinymce.models.HTMLField(null=True, verbose_name='Observații'),
        ),
    ]
