# Generated by Django 4.0.3 on 2022-05-20 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_ventas_options_rename_monto_ventas_montosadasd_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ventas',
            options={'ordering': ['monto'], 'verbose_name': 'Monto', 'verbose_name_plural': 'Montos'},
        ),
        migrations.RenameField(
            model_name='ventas',
            old_name='montosadasd',
            new_name='monto',
        ),
        migrations.AlterModelTable(
            name='ventas',
            table='Venta',
        ),
    ]