# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 05:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_update_authors', 'Can manipulate authors table'),)},
        ),
    ]