# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0002_inscripcion_participante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
