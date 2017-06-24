# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0003_auto_20170531_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secret_owner', to='logreg.UserDB'),
        ),
    ]