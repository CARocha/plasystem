# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-02 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subsectores', '0007_auto_20171002_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informemensual',
            name='alcanzados_mes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='gastos_mes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='informacion_cualitativa',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='momento_indicador',
            field=models.IntegerField(blank=True, choices=[(1, 'Proceso'), (2, 'Desarrollo'), (3, 'Cumplido')], null=True),
        ),
        migrations.AlterField(
            model_name='informemensual',
            name='subir_archivo',
            field=models.FileField(blank=True, null=True, upload_to='informeMensual'),
        ),
    ]
