# Generated by Django 5.0.6 on 2024-06-23 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_rename_total_detalle_boleta_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleta',
            name='id_cliente',
        ),
    ]
