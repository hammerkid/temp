# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest_book', '0006_auto_20181026_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]