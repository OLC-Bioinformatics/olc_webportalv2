# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-14 19:50
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowbat', '0002_sequencingrun_emails_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequencingrun',
            name='emails_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=50), blank=True, default=[], size=None),
        ),
    ]
