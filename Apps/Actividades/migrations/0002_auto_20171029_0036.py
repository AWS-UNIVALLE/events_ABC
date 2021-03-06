# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0001_initial'),
        ('Eventos', '0001_initial'),
        ('Actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='participante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Usuario'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eventos.Evento'),
        ),
    ]
