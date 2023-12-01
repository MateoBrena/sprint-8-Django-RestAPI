from .models import Direccion
from .serializers import DireccionSerializer
from Clientes.models import Cliente
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.
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
    
class DireccionDetail(generics.RetrieveAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    

    