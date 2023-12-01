from .models import Cuenta
from .serializers import CuentaSerializer
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class CuentaDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer

class CuentasCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        cuentas = Cuenta.objects.filter(cliente = pk)
        serializer = CuentaSerializer(cuentas, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)