# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='isFavorite',
            field=models.BooleanField(default=False),
        ),
    ]
