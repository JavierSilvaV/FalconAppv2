# Generated by Django 4.0.3 on 2022-05-20 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_venta_usuario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]
