# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-26 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_ratings', '0016_item_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
