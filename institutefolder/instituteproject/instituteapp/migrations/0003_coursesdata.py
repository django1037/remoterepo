# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-25 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0002_contactdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('course_dur', models.IntegerField()),
                ('course_fee', models.IntegerField()),
                ('start_date', models.DateField(max_length=100)),
                ('start_time', models.TimeField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('trainer_exp', models.IntegerField()),
            ],
        ),
    ]
