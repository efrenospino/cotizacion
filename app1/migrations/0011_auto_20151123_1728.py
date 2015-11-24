# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20151121_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='bono',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
