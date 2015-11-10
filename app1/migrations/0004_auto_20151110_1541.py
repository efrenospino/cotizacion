# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_detallecotizacion_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idEstadoCliente',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idTipoId',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='idEstadoCotizacion',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='cantidad',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='detallecotizacion',
            name='idEstadoDetalleCotizacion',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='idEstadoEmpleado',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='idTipoId',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='idEstadoEmpresa',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idEstadoProducto',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='idUnidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='idEstadoServicio',
            field=models.PositiveIntegerField(),
        ),
    ]
