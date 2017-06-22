# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0002_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='secret_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secret_likes', to='secrets.Secret'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='logreg.UserDB'),
        ),
    ]
