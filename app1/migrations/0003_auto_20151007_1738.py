# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20151007_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcotizacion',
            name='producto',
            field=models.ForeignKey(to='app1.Producto', blank=True),
        ),
        migrations.AlterField(
            model_name='itemcotizacion',
            name='servicio',
            field=models.ForeignKey(to='app1.Servicio', blank=True),
        ),
    ]
