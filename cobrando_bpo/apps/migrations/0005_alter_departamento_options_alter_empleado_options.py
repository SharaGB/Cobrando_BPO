# Generated by Django 4.1.5 on 2023-01-12 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_departamento_presupuesto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['codigo'], 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['codigo'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
    ]
