# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=100),
        ),
    ]
