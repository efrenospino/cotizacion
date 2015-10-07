# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('eliminado', models.BooleanField(default=False)),
                ('cotizacion', models.ForeignKey(to='app1.Cotizacion')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=255, blank=True)),
                ('precio', models.FloatField()),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='idUnidad',
        ),
        migrations.AddField(
            model_name='itemcotizacion',
            name='producto',
            field=models.ForeignKey(to='app1.Producto', null=True),
        ),
        migrations.AddField(
            model_name='itemcotizacion',
            name='servicio',
            field=models.ForeignKey(to='app1.Servicio', null=True),
        ),
        migrations.AddField(
            model_name='detallecotizacion',
            name='itemCotizacion',
            field=models.ForeignKey(to='app1.ItemCotizacion'),
        ),
    ]
