# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-07 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0004_auto_20160907_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='articlereg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('timestart', models.DateTimeField()),
                ('articlename', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=150)),
                ('minbid', models.FloatField(default=0)),
                ('image', models.ImageField(default='article_images/<built-in function id>.jpg', upload_to='article_images/')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.UserDetail')),
            ],
        ),
        migrations.CreateModel(
            name='banned_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highestbid', models.FloatField(default=0)),
                ('articleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.articlereg')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.UserDetail')),
            ],
        ),
    ]