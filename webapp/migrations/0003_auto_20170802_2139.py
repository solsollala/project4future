# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='organization',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='passwd',
            field=models.CharField(max_length=15),
        ),
    ]