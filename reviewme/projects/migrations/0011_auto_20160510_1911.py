# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160510_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='assined_time',
            new_name='assigned_time',
        ),
    ]