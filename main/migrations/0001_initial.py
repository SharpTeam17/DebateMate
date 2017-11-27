# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 01:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('initial_post_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('source', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1)),
                ('initial_post_date', models.DateTimeField(auto_now_add=True)),
                ('last_edited_date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('source', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyDebate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.TextField()),
                ('status', models.CharField(choices=[('N', 'Not started'), ('O', 'Open'), ('V', 'In voting'), ('C', 'Complete')], default='N', max_length=1)),
                ('is_current_debate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_side', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('N', 'Not on side')], default='N', max_length=1)),
                ('current_role', models.CharField(choices=[('S', 'Spectator'), ('D', 'Debater'), ('M', 'Moderator')], default='S', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_debate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DailyDebate'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Argument'),
        ),
        migrations.AddField(
            model_name='argument',
            name='parent_debate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.DailyDebate'),
        ),
    ]
