# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='introduction',
            field=models.CharField(default=datetime.datetime(2016, 6, 4, 3, 29, 56, 118100, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]
