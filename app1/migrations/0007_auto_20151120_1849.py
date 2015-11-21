# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20151120_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='identificacion',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='identificacion',
            field=models.PositiveIntegerField(),
        ),
    ]
