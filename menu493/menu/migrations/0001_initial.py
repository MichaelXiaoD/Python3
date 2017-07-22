# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 17:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=40)),
                ('type', models.CharField(db_column='type', max_length=10)),
                ('price', models.FloatField(db_column='price', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplyDate', models.DateField(db_column='supply_date', default=datetime.date(2017, 7, 21))),
                ('supplyTime', models.CharField(db_column='supply_time', default='lunch', max_length=10)),
                ('dishs', models.ManyToManyField(to='menu.Dish')),
            ],
        ),
    ]
