# Generated by Django 3.2.4 on 2022-03-31 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_productos_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.ImageField(null=True, upload_to='marcas')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'db_table': 'marcas',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='productos',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.marcas'),
        ),
    ]
