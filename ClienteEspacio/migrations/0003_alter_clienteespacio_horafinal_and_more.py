# Generated by Django 5.1.1 on 2024-09-14 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClienteEspacio', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clienteespacio',
            name='HoraFinal',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clienteespacio',
            name='HoraReserva',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
