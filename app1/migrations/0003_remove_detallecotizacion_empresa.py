# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_cotizacion_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallecotizacion',
            name='empresa',
        ),
    ]
