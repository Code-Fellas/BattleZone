# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0006_delete_problems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languages',
            old_name='version',
            new_name='hackerrank_name',
        ),
    ]
