# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chair', '0003_chairtype_part_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairtype',
            name='part_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parts.PartType'),
        ),
    ]
