# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-09 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20160909_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banned_user',
            name='userid',
            field=models.IntegerField(),
        ),
    ]
