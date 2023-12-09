from rest_framework import serializers
from .models import Transferencia


class TransferenciaSerializer(serializers.ModelSerializer):
    cliente =  serializers.ReadOnlyField(source = 'cliente.name')
    class Meta:
        model = Transferencia
        fields = "__all__"
        depth = 1
        read_only_fields = ("id",)