# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_spec'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='example',
            field=models.URLField(blank=True, null=True),
        ),
    ]
