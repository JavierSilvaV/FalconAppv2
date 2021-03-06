# Generated by Django 4.0.3 on 2022-05-20 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0022_marcas_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Nombre',
                'verbose_name_plural': 'Nombres',
                'db_table': 'nombre_comuna',
                'ordering': ['nombre_comuna'],
            },
        ),
        migrations.CreateModel(
            name='Metodo_Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_metodo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Nombre',
                'verbose_name_plural': 'Nombres',
                'db_table': 'nombre_metodo',
                'ordering': ['nombre_metodo'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Nombre',
                'verbose_name_plural': 'Nombres',
                'db_table': 'nombre_region',
                'ordering': ['nombre_region'],
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('email_venta', models.CharField(max_length=50)),
                ('fecha_venta', models.DateField()),
                ('estado_venta', models.CharField(max_length=50)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Monto',
                'verbose_name_plural': 'Montoa',
                'db_table': 'monto',
                'ordering': ['monto'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_provincia', models.CharField(max_length=50)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.region')),
            ],
            options={
                'verbose_name': 'Nombre',
                'verbose_name_plural': 'Nombres',
                'db_table': 'nombre_provincia',
                'ordering': ['nombre_provincia'],
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.comuna')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
                'db_table': 'comuna',
                'ordering': ['comuna'],
            },
        ),
        migrations.AddField(
            model_name='comuna',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.provincia'),
        ),
    ]
