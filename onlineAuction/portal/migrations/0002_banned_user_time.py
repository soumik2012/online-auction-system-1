# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banned_user',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
