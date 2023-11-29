# Create your views here.

from rest_framework import generics, permissions, viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from Sucursales.models import Sucursal
from Sucursales.serializers import SucursalSerializer
from Cuentas.models import Cuenta
from Cuentas.serializers import CuentaSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'clientes': reverse('clientes-list', request=request, format=format),
        'sucursales': reverse('sucursales-list', request=request, format=format)
    })
class ClienteList(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class SucursalList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class CuentaList(generics.ListAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

