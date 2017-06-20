# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0002_auto_20170620_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acuerdocomercial',
            name='periodo',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='c.3.Periodo del contrato'),
        ),
        migrations.AlterField(
            model_name='acuerdocomercial',
            name='tipo_contrato',
            field=models.IntegerField(blank=True, choices=[(1, 'c.1) Contrato escrito'), (2, 'c.2) Contrato verbal')], null=True),
        ),
    ]
