from rest_framework import permissions, status
from rest_framework.views import APIView
from Clientes.models import Cliente
from rest_framework.response import Response
from .models import Pagos
from .serializers import PagoSerializer

# Create your views here.

class PagoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        pago = Pagos.objects.filter(pk = pk)
        serializer = PagoSerializer(pago, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    

class PagosCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        pagos = Pagos.objects.filter(cliente = pk)
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)