# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-31 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_order_quantity_of_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity_of_item',
        ),
    ]
