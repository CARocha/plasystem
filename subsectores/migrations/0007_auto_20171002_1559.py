# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-02 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsectores', '0006_auto_20171002_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datosgenerales',
            options={'verbose_name': 'Dato General (subsector)', 'verbose_name_plural': 'Datos Generales (subsectores)'},
        ),
        migrations.AlterModelOptions(
            name='informemensual',
            options={'verbose_name': 'Informe trimestral', 'verbose_name_plural': 'Informes trimestrales'},
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='resultados',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
