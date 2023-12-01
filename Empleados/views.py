from .models import Empleado
from .serializers import EmpleadoSerializer
from rest_framework import generics, permissions

# Create your views here.

class EmpleadoDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer