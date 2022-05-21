# Generated by Django 3.2.4 on 2022-05-21 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_detalle_ingreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_ingreso',
            name='ingreso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.ingreso'),
            preserve_default=False,
        ),
    ]