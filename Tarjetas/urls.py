from django.urls import path
from .views import TarjetaDetail, TarjetasCliente

urlpatterns = [
    path('api/tarjetas/<int:pk>', TarjetaDetail.as_view(), name='tarjeta-detail'),
    path('api/clientes/<int:pk>/tarjetas/', TarjetasCliente.as_view(), name='clientes-tarjetas')
]