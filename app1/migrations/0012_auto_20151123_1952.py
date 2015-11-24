# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20151123_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='descuento',
            field=models.PositiveIntegerField(default=16),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='bono',
            field=models.PositiveIntegerField(default=13),
        ),
    ]
