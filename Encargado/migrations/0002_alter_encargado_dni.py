# Generated by Django 5.1.1 on 2024-09-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Encargado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encargado',
            name='Dni',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
