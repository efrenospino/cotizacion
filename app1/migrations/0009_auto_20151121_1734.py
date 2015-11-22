# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20151120_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametro',
            name='estadoParametro',
        ),
        migrations.RemoveField(
            model_name='valorparametro',
            name='estadoValorParametro',
        ),
        migrations.AddField(
            model_name='parametro',
            name='estado',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='valorparametro',
            name='estado',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='empleado',
            field=models.ForeignKey(to='app1.Empleado'),
        ),
        migrations.AlterField(
            model_name='valorparametro',
            name='orden',
            field=models.PositiveIntegerField(),
        ),
    ]
