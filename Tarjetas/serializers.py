from rest_framework import serializers
from .models import Tarjeta


class TarjetaSerializer(serializers.ModelSerializer):
    cliente =  serializers.ReadOnlyField(source = 'cliente.name')
    class Meta:
        model = Tarjeta
        fields = "__all__"
        depth = 1
        read_only_fields = ("id",)