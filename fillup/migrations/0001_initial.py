# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_num', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('course', models.TextField()),
                ('year', models.TextField()),
            ],
        ),
    ]
