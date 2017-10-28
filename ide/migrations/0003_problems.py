# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ide', '0002_auto_20171027_1732'),
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
