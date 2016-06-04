# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='introduction',
            field=models.CharField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
