# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_tornadoes'),
    ]

    operations = [
        migrations.CreateModel(
            name='HockeyPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playername', models.CharField(max_length=4)),
                ('position', models.CharField(max_length=20)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.HockeyTeam')),
            ],
        ),
    ]
