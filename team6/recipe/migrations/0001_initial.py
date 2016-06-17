# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('visitor', models.CharField(max_length=20)),
                ('private', models.BooleanField(default=False)),
                ('content', models.CharField(blank=True, max_length=300)),
                ('date_time', models.DateTimeField()),
                ('reply', models.CharField(blank=True, max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('chinesename', models.CharField(max_length=20)),
                ('englishname', models.CharField(max_length=20)),
                ('schoolid', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=30)),
                ('introduction', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('index', models.DecimalField(max_digits=2, decimal_places=0)),
                ('image', models.FileField(upload_to='static/images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingrediant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('index', models.DecimalField(max_digits=2, decimal_places=0)),
                ('food', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('introduction', models.CharField(blank=True, max_length=250)),
                ('menu', models.ForeignKey(to='recipe.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('index', models.DecimalField(max_digits=2, decimal_places=0)),
                ('content', models.CharField(max_length=200)),
                ('recipe', models.ForeignKey(to='recipe.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ingrediant',
            name='recipe',
            field=models.ForeignKey(to='recipe.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='recipe',
            field=models.ForeignKey(to='recipe.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(to='recipe.Recipe'),
            preserve_default=True,
        ),
    ]
