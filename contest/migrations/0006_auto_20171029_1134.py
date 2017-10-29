# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_testcases_is_sample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='judge_solution',
        ),
        migrations.AlterField(
            model_name='contests',
            name='end_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contests',
            name='start_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='marks',
            field=models.IntegerField(default=20),
        ),
    ]
