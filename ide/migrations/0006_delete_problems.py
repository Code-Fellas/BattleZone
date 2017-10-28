# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0005_problems'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Problems',
        ),
    ]
