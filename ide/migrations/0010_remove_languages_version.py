# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0009_auto_20171029_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languages',
            name='version',
        ),
    ]
