# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chair', '0011_auto_20180731_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairtype',
            name='parent_id',
            field=models.IntegerField(),
        ),
    ]
