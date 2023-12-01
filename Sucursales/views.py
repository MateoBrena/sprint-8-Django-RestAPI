from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sucursal
from Clientes.models import Cliente
from .serializers import SucursalSerializer
from Prestamos.serializers import PrestamoSerializer
from Prestamos.models import Prestamo

class SucursalPrestamos(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(pk = pk).first()
        clientes = Cliente.objects.filter(branch = sucursal.id)
        losClientes = clientes.values_list("id", flat=True)
        prestamos = Prestamo.objects.filter(cliente__in = losClientes)
        serializer = PrestamoSerializer(prestamos, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)