from rest_framework import permissions, status
from rest_framework.views import APIView
from Clientes.models import Cliente
from rest_framework.response import Response
from .models import Transferencia
from .serializers import TransferenciaSerializer

# Create your views here.

class TransferDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        transferencias = Transferencia.objects.filter(pk = pk)
        serializer = TransferenciaSerializer(transferencias, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    

class TransferenciasCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        transferencias = Transferencia.objects.filter(cliente = pk)
        serializer = TransferenciaSerializer(transferencias, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)