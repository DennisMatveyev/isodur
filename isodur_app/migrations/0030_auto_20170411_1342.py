# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-11 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isodur_app', '0029_auto_20170411_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product1',
            name='product_photo',
        ),
        migrations.AddField(
            model_name='product1',
            name='products',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
