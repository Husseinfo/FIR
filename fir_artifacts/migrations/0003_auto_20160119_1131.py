# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir_artifacts', '0002_create_artifacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='hashes',
            field=models.ManyToManyField(blank=True, to='fir_artifacts.Artifact'),
        ),
    ]