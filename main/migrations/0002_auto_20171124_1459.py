# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-24 20:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_side', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('N', 'Not on side')], default='N', max_length=1)),
                ('current_role', models.CharField(choices=[('S', 'Spectator'), ('D', 'Debater'), ('M', 'Moderator')], default='S', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='argument',
            name='source',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dailydebate',
            name='is_current_debate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailydebate',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='argument',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='argument',
            name='initial_post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='argument',
            name='last_edited_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='initial_post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='last_edited_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dailydebate',
            name='status',
            field=models.CharField(choices=[('N', 'Not started'), ('O', 'Open'), ('V', 'In voting'), ('C', 'Complete')], default='N', max_length=1),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
