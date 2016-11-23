# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
