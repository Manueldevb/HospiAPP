# Generated by Django 4.1.1 on 2022-09-14 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospiApp', '0004_paciente_medico'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliarDesignado',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('numTelefono', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('paciente', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospiApp.paciente')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
