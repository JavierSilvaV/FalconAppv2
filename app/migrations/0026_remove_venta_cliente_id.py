# Generated by Django 4.0.3 on 2022-05-20 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_venta_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cliente_id',
        ),
    ]
