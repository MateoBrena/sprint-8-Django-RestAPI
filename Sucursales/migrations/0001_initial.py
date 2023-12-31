# Generated by Django 4.2.7 on 2023-11-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Direcciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Direcciones.direccion')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
            },
        ),
    ]
