# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contest_code', models.CharField(unique=True, max_length=20)),
                ('date', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('duration', models.BigIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'contests',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_code', models.CharField(max_length=20)),
                ('problem_statement', models.TextField()),
                ('total_samples', models.IntegerField()),
                ('test_inputs', models.TextField()),
                ('test_outputs', models.TextField()),
                ('test_case_marks', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(to='contest.Contests')),
            ],
            options={
                'db_table': 'problems',
            },
        ),
    ]
