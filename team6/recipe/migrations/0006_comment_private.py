# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]