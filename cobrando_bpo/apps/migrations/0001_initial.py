# Generated by Django 4.1.5 on 2023-01-12 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('presupuesto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nif', models.CharField(max_length=9, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('codigo_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.departamento')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['nombre'],
            },
        ),
    ]
