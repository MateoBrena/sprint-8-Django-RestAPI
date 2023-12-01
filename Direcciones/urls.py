from django.urls import path
from .views import ClienteDireccion, DireccionDetail

urlpatterns = [
    path('api/clientes/<int:pk>/direccion/', ClienteDireccion.as_view(), name='cliente-direccion'),
    path('api/direcciones/<int:pk>/', DireccionDetail.as_view(), name='direccion-detail'),
]