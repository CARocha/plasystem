# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0005_auto_20170703_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producencomercializan',
            name='unidad_medida',
        ),
        migrations.AddField(
            model_name='producencomercializan',
            name='precio_promedio_certificada',
            field=models.FloatField(default=0),
        ),
    ]
