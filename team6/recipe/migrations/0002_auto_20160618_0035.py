# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-17 16:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='introduction',
        ),
    ]
