# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 16:00
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('noleggi', '0005_remove_auto_miniatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='immagine',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='staticfiles/images/auto'),
        ),
    ]
