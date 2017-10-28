# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0003_auto_20171028_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testcases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('marks', models.IntegerField()),
            ],
            options={
                'db_table': 'testcases',
            },
        ),
        migrations.RemoveField(
            model_name='problem',
            name='test_case_marks',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='test_inputs',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='test_outputs',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='total_samples',
        ),
        migrations.AddField(
            model_name='testcases',
            name='problem',
            field=models.ForeignKey(to='contest.Problem'),
        ),
    ]
