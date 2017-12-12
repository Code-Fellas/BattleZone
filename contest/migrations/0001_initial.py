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
                ('title', models.CharField(default=None, max_length=255)),
                ('contest_code', models.CharField(unique=True, max_length=20)),
                ('date', models.CharField(max_length=255)),
                ('start_time', models.CharField(max_length=255)),
                ('end_time', models.CharField(max_length=255)),
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
                ('title', models.CharField(default=b'A', max_length=255)),
                ('problem_code', models.CharField(max_length=20)),
                ('problem_statement', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(to='contest.Contests')),
            ],
            options={
                'db_table': 'problems',
            },
        ),
        migrations.CreateModel(
            name='Testcases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('is_sample', models.BooleanField(default=False)),
                ('marks', models.IntegerField(default=20)),
                ('problem', models.ForeignKey(to='contest.Problem')),
            ],
            options={
                'db_table': 'testcases',
            },
        ),
    ]
