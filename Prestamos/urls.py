from django.urls import path
from .views import PrestamoDetail, PrestamosCliente

urlpatterns = [
    path('api/prestamos/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail'),
    path('api/clientes/<int:pk>/prestamos/', PrestamosCliente.as_view(), name='clientes-prestamos')
]