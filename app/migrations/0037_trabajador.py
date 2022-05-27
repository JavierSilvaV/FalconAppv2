# Generated by Django 4.0.3 on 2022-05-20 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_rename_usuario_id_venta_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.IntegerField(max_length=9)),
                ('email', models.EmailField(max_length=50)),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.BinaryField()),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.venta')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
                'db_table': 'Trabajador',
                'ordering': ['nombre'],
            },
        ),
    ]
