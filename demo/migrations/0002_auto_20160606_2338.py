# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='feedback',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intro',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='intro',
            name='note',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intro',
            name='reviewing',
            field=models.BooleanField(default=False),
        ),
    ]