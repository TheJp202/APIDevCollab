# Generated by Django 5.1.1 on 2024-09-14 22:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Estacionamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dni', models.CharField(max_length=8)),
                ('Nombre', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=128)),
                ('FechaRegistro', models.DateField(default=datetime.date.today)),
                ('Estacionamiento', models.ForeignKey(db_column='IdEstacionamiento', on_delete=django.db.models.deletion.CASCADE, to='Estacionamiento.estacionamiento')),
            ],
        ),
    ]
