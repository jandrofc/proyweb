# Generated by Django 5.0.6 on 2024-06-25 03:19

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emitida', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('iva', models.IntegerField()),
                ('total_neto', models.IntegerField()),
                ('total_a_pagar', models.IntegerField()),
                ('estado_pago', models.CharField(choices=[('P', 'Pagado'), ('N', 'No Pagado'), ('E', 'Pendiente')], default='E', max_length=1)),
                ('estado_despacho', models.CharField(choices=[('D', 'Despachado'), ('N', 'No Despachado'), ('R', 'Recibido')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=150, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=150)),
                ('imagen', models.ImageField(blank=True, default='productos/icono.jpeg', null=True, upload_to='productos')),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('subtotal', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('id_boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='tienda.boleta')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]
