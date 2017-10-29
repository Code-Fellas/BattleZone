# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0007_auto_20171029_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languages',
            name='hackerrank_name',
        ),
        migrations.AddField(
            model_name='languages',
            name='version',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
