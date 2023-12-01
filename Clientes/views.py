# Create your views here.
from rest_framework import generics, permissions, status
from .models import Cliente
from .serializers import ClienteSerializer
from Direcciones.models import Direccion
from Direcciones.serializers import DireccionSerializer
from Sucursales.models import Sucursal
from Sucursales.serializers import SucursalSerializer
from Cuentas.models import Cuenta
from Cuentas.serializers import CuentaSerializer
from Tarjetas.models import Tarjeta
from Tarjetas.serializers import TarjetaSerializer
from Prestamos.models import Prestamo
from Prestamos.serializers import PrestamoSerializer
from Empleados.models import Empleado
from Empleados.serializers import EmpleadoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'clientes': reverse('clientes-list', request=request, format=format),
        'sucursales': reverse('sucursales-list', request=request, format=format),
        'cuentas': reverse('cuentas-list', request=request, format=format),
        'tarjetas': reverse('tarjetas-list', request=request, format=format),
        'prestamos': reverse('prestamos-list', request=request, format=format),
        'direcciones': reverse('direcciones-list', request=request, format=format),
        'empleados': reverse('empleados-list', request=request, format=format),
    })
class ClientesList(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DireccionesList(generics.ListAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class CuentasList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class TarjetasList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

class PrestamosList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class EmpleadosList(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
