from rest_framework import serializers
from .models import Cuenta


class CuentaSerializer(serializers.ModelSerializer):
    cliente =  serializers.ReadOnlyField(source = 'cliente.name')
    class Meta:
        model = Cuenta
        fields = "__all__"
        depth = 1
        read_only_fields = ("id",)