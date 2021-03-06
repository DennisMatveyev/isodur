# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('isodur_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productphoto',
            name='add_to_slider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='pub_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectphoto',
            name='add_to_slider',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keyword',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='isodur_app.Section'),
        ),
    ]
