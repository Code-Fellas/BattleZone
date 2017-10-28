# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_auto_20171028_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcases',
            name='is_sample',
            field=models.BooleanField(default=False),
        ),
    ]
