# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20171126_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='argument',
            name='reportedDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='isReported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='reasonForBeingReported',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='reportedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
