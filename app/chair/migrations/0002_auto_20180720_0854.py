# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-20 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chair', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chairtype',
            old_name='chairtype',
            new_name='chair',
        ),
    ]
