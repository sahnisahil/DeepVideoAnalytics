# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-27 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0017_auto_20170505_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
