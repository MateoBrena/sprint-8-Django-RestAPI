from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prestamo
from Clientes.models import Cliente
from .serializers import PrestamoSerializer
from Cuentas.models import Cuenta

# Create your views here.
class PrestamoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
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