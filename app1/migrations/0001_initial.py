# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=15)),
                ('razonSocial', models.CharField(max_length=200, blank=True)),
                ('idTipoId', models.IntegerField()),
                ('nombres', models.CharField(max_length=100, blank=True)),
                ('apellidos', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('direccion', models.CharField(max_length=100, blank=True)),
                ('idEstadoCliente', models.IntegerField()),
                ('telefonos', models.CharField(max_length=100, blank=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('idEstadoCotizacion', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(to='app1.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('idEstadoDetalleCotizacion', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
                ('cotizacion', models.ForeignKey(to='app1.Cotizacion')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=15)),
                ('idTipoId', models.IntegerField()),
                ('nombres', models.CharField(max_length=100, blank=True)),
                ('apellidos', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('direccion', models.CharField(max_length=100, blank=True)),
                ('idEstadoEmpleado', models.IntegerField()),
                ('telefonos', models.CharField(max_length=100, blank=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=15)),
                ('razonSocial', models.CharField(max_length=200, blank=True)),
                ('direccion', models.CharField(max_length=100, blank=True)),
                ('idEstadoEmpresa', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('estadoParametro', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('idUnidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('idEstadoProducto', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(to='app1.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('precio', models.FloatField()),
                ('idEstadoServicio', models.IntegerField()),
                ('eliminado', models.BooleanField(default=False)),
                ('empresa', models.ForeignKey(to='app1.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='ValorParametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=30)),
                ('orden', models.CharField(max_length=3)),
                ('estadoValorParametro', models.CharField(max_length=1)),
                ('parametro', models.ForeignKey(to='app1.Parametro')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='empresa',
            field=models.ForeignKey(to='app1.Empresa'),
        ),
        migrations.AddField(
            model_name='detallecotizacion',
            name='empresa',
            field=models.ForeignKey(to='app1.Empresa'),
        ),
        migrations.AddField(
            model_name='detallecotizacion',
            name='producto',
            field=models.ForeignKey(blank=True, to='app1.Producto', null=True),
        ),
        migrations.AddField(
            model_name='detallecotizacion',
            name='servicio',
            field=models.ForeignKey(blank=True, to='app1.Servicio', null=True),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='empleado',
            field=models.ForeignKey(to='app1.Empleado'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='empresa',
            field=models.ForeignKey(to='app1.Empresa'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(to='app1.Empresa'),
        ),
    ]
