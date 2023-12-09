from rest_framework import serializers
from .models import Pagos


class PagoSerializer(serializers.ModelSerializer):
    cliente =  serializers.ReadOnlyField(source = 'cliente.name')
    class Meta:
        model = Pagos
        fields = "__all__"
        depth = 1
        read_only_fields = ("id",)