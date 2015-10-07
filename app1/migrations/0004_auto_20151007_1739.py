# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20151007_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcotizacion',
            name='producto',
            field=models.ForeignKey(blank=True, to='app1.Producto', null=True),
        ),
        migrations.AlterField(
            model_name='itemcotizacion',
            name='servicio',
            field=models.ForeignKey(blank=True, to='app1.Servicio', null=True),
        ),
    ]
