# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targa', models.CharField(max_length=7, unique=True)),
                ('modello', models.CharField(max_length=50)),
                ('alimentazione', models.CharField(choices=[('B', 'benzina'), ('G', 'gasolio'), ('M', 'metano')], max_length=1)),
                ('colore', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Auto',
            },
        ),
        migrations.CreateModel(
            name='Noleggio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operatore', models.CharField(choices=[('01', 'operatore1'), ('02', 'operatore2'), ('03', 'operatore3')], max_length=2)),
                ('datauscita', models.DateField(verbose_name='data uscita')),
                ('dataentrata', models.DateField(blank=True, null=True, verbose_name='data entrata')),
                ('fkAuto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noleggi.Auto', verbose_name='targa')),
            ],
            options={
                'verbose_name_plural': 'Noleggi',
            },
        ),
    ]
