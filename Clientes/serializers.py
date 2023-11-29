from rest_framework import serializers
from .models import Cliente
from Cuentas.models import Cuenta

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = "__all__"
        depth = 2
        read_only_fields = ("id",)

