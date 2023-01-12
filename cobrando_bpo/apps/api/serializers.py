from rest_framework import serializers
from apps.models import Departamento, Empleado


class DepartamentoSerializer(serializers.ModelSerializer):
    """Serializer based in Departamento model"""
    class Meta:
        model = Departamento
        fields = ('codigo', 'nombre', 'presupuesto')


class EmpleadoSerializer(serializers.ModelSerializer):
    """Serializer based in Empleado model"""
    serializer_class = DepartamentoSerializer

    class Meta:
        model = Empleado
        fields = ('codigo', 'nif', 'nombre', 'apellido1', 'apellido2', 'codigo_departamento')
