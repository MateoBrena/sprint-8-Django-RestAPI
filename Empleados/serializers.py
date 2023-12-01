from rest_framework import serializers
from .models import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = "__all__"
        depth = 2
        read_only_fields = ("id",)