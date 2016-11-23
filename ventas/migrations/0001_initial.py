# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('codigo', models.CharField(max_length=7)),
                ('nombre', models.CharField(max_length=15)),
                ('imagen', models.ImageField(upload_to='photo/')),
                ('marca', models.CharField(default='CO', choices=[('CO', 'Comida'), ('RO', 'Ropa'), ('ZA', 'Zapatos'), ('JU', 'Juegos')], max_length=2)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('existencia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('dpi', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('productos', models.ManyToManyField(to='ventas.Producto', through='ventas.Compra')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ForeignKey(to='ventas.Producto'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(to='ventas.Usuario'),
        ),
    ]
