# Generated by Django 4.2.7 on 2023-12-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuentas', to='Clientes.cliente'),
        ),
    ]
