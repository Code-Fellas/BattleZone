# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0008_auto_20171029_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='languages',
            name='hackerrank_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='languages',
            name='version',
            field=models.CharField(max_length=20),
        ),
    ]
