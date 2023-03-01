# Generated by Django 4.1.1 on 2022-09-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospiApp', '0002_paciente_delete_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numTelefono', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=50)),
                ('registro', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
