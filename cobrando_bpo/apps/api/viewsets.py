from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.models import Departamento, Empleado
from apps.api.serializers import DepartamentoSerializer, EmpleadoSerializer


class DepartamentoViewset(ModelViewSet):
    serializer_class = DepartamentoSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return Departamento.objects.all()
        else:
            return Departamento.objects.filter(codigo=pk).first()

    def list(self, request):
        departamento_serializer = self.get_serializer(
            self.get_queryset(), many=True)
        return Response(departamento_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Department successfully created!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            departamento_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if departamento_serializer.is_valid():
                departamento_serializer.save()
                return Response(departamento_serializer.data, status=status.HTTP_200_OK)
            return Response(departamento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        departamento = self.get_queryset().filter(codigo=pk).first()
        if departamento:
            departamento.delete()
            return Response({"Message": "Department successfully eliminated!"}, status=status.HTTP_200_OK)
        return Response({"Message": "Department doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


class EmpleadoViewSet(ModelViewSet):
    serializer_class = EmpleadoSerializer

    def get_queryset(self, pk=None):
        if pk == None:
            return Empleado.objects.all()
        else:
            return Empleado.objects.filter(codigo=pk).first()
            # return Empleado.objects.filter(pk=self.request.user.profile.codigo)

    def list(self, request):
        empleado_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(empleado_serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Employee successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            empleado_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if empleado_serializer.is_valid():
                empleado_serializer.save()
                return Response(empleado_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        empleado = self.get_queryset().filter(codigo=pk).first()
        if empleado:
            empleado.delete()
            return Response({"Message": "Employee successfully eliminated"}, status=status.HTTP_200_OK)
        return Response({"Message": "Employee doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
