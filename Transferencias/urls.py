from django.urls import path
from .views import TransferDetail, TransferenciasCliente

urlpatterns = [
    path('api/transferencias/<int:pk>/', TransferDetail.as_view(), name='transferencia-detail'),
    path('api/clientes/<int:pk>/transferencias/', TransferenciasCliente.as_view(), name='clientes-transferencias')
]