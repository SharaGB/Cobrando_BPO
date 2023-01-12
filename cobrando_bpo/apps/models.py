from django.db import models


class Departamento(models.Model):
    """ Template for the Department table """
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['codigo']

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    """ Template for the Employee table """
    codigo = models.AutoField(primary_key=True)
    nif = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido1 = models.CharField(max_length=100)
    apellido2 = models.CharField(max_length=100)
    codigo_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['codigo']

    def __str__(self):
        return f'{self.nombre} {self.apellido1} - {self.nif} - {self.codigo_departamento}'
