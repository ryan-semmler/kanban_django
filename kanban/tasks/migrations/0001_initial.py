# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[(1, 'not started'), (2, 'in progress'), (3, 'completed')], default='(1, not started)', max_length=20)),
                ('priority', models.CharField(choices=[(1, 'low priority'), (2, 'medium-rare priority'), (3, 'medium priority'), (4, 'medium-well priority'), (5, 'top priority')], default='(1, low priority)', max_length=20)),
            ],
        ),
    ]
