# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-25 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_remove_courseorg_classic_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]