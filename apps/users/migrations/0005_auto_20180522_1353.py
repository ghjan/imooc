# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180519_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='/static/images/default.png', upload_to='image/%Y/%m'),
        ),
    ]
