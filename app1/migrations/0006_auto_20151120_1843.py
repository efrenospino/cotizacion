# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_auto_20151118_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='empleado',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
