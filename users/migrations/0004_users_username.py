# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171221_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
