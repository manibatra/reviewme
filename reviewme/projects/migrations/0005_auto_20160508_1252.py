# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_project_finished'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('returned_on', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='project',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='project',
            name='returned_on',
        ),
        migrations.RemoveField(
            model_name='project',
            name='student',
        ),
        migrations.RemoveField(
            model_name='project',
            name='submitted_on',
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='none', max_length=132),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='submission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
