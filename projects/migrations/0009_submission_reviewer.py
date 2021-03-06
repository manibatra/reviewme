# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 14:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0008_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
