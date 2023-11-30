# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
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
    })
class ClientesList(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DireccionesList(generics.ListAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class ClienteDireccion(APIView):

    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk = pk).first()
        direccion = Direccion.objects.filter(pk = cliente.direccion.id)
        serializer = DireccionSerializer(direccion, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def put(self, request, pk):
        cliente = Cliente.objects.filter(pk = pk).first()
        direccion = Direccion.objects.get(pk = cliente.direccion.id) 
        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    

class CuentasCliente(APIView):
    
    def get(self, request, pk):
        cuentas = Cuenta.objects.filter(cliente = pk)
        serializer = CuentaSerializer(cuentas, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class SucursalesList(generics.ListAPIView):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer

class SucursalPrestamos(APIView):
    def get(self, request, pk):
        sucursal = Sucursal.objects.filter(pk = pk).first()
        clientes = Cliente.objects.filter(branch = sucursal.id)
        losClientes = clientes.values_list("id", flat=True)
        prestamos = Prestamo.objects.filter(cliente__in = losClientes)
        serializer = PrestamoSerializer(prestamos, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class CuentasList(generics.ListAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class CuentaDetail(generics.RetrieveAPIView):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class TarjetasList(generics.ListAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

class TarjetaDetail(generics.RetrieveAPIView):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

class TarjetasCliente(APIView):
    
    def get(self, request, pk):
        cuentas = Tarjeta.objects.filter(cliente = pk)
        serializer = TarjetaSerializer(cuentas, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class PrestamosList(generics.ListAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

class PrestamoDetail(APIView):

    def get(self, request, pk):
        prestamos = Prestamo.objects.filter(pk = pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def delete(self, request, pk):
        prestamo = Prestamo.objects.filter(pk = pk).first()
        cuenta = Cuenta.objects.filter(cliente = prestamo.cliente, tipo__exact = 1).first()
        if prestamo:
            serializer = PrestamoSerializer(prestamo)
            cuenta.balance = cuenta.balance - int(prestamo.monto)
            cuenta.save()
            prestamo.delete()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(status= status.HTTP_404_NOT_FOUND)

class PrestamosCliente(APIView):
    
    def get(self, request, pk):
        prestamos = Prestamo.objects.filter(cliente = pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request, pk, format = None):
        cuenta = Cuenta.objects.filter(cliente = pk, tipo__exact = 1).first()
        serializer = PrestamoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(cliente = Cliente.objects.filter(pk=pk).first())
            cuenta.balance = cuenta.balance + int(serializer.data['monto'])
            cuenta.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
