# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pw_hash',
            field=models.CharField(default='t3mpPassword', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
