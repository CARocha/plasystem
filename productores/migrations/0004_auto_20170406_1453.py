# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productores', '0003_productor_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivo',
            name='hortaliza',
        ),
        migrations.AddField(
            model_name='cultivo',
            name='tipo',
            field=models.IntegerField(choices=[(1, 'Caf\xe9'), (2, 'Cacao'), (3, 'Hortaliza')], default=1),
            preserve_default=False,
        ),
    ]
