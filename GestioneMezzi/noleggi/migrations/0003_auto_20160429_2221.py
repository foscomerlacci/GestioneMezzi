# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noleggi', '0002_auto_20160428_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='immagine',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/images/auto'),
        ),
    ]
