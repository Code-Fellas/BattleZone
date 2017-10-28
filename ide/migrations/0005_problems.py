# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0004_delete_problems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_statement', models.TextField()),
            ],
        ),
    ]
