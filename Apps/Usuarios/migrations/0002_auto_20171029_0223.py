# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 02:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='rol',
            new_name='cargo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombres',
        ),
    ]