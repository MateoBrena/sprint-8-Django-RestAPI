from rest_framework import serializers
from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    cliente =  serializers.ReadOnlyField(source = 'cliente.name')
    class Meta:
        model = Prestamo
        fields = "__all__"
        depth = 1
        read_only_fields = ("id",)