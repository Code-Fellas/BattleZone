# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_problem_judge_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='title',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.CharField(default=b'A', max_length=255),
        ),
    ]
