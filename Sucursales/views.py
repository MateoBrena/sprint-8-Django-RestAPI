# Create your views here.

from rest_framework import generics, permissions, viewsets

from .models import Sucursal
from .serializers import SucursalSerializer

class SucursalList(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer