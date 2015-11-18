# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20151110_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='empresa',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idEstadoCliente',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='idEstadoCotizacion',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='idEstadoDetalleCotizacion',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='idEstadoEmpleado',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idEstadoProducto',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='idEstadoServicio',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
