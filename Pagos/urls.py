from django.urls import path
from .views import PagoDetail, PagosCliente

urlpatterns = [
    path('api/pagos/<int:pk>/', PagoDetail.as_view(), name='pago-detail'),
    path('api/clientes/<int:pk>/pagos/', PagosCliente.as_view(), name='clientes-pagos')
]