# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20151120_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='email',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='nombres',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]
