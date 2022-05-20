# Generated by Django 4.0.3 on 2022-05-20 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo_comprobante', models.CharField(max_length=50)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.proveedor')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
                'db_table': 'Ingreso',
                'ordering': ['fecha'],
            },
        ),
    ]
