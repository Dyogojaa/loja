
from django.urls import include, path
from .views import Pagar, FecharPedido, Detalhe

app_name = 'pedido'

urlpatterns = [    
    path('',Pagar.as_view(), name='pagar'),
    path('fecharpedido/',FecharPedido.as_view(), name='fecharpedido'),
    path('detalhe/',Detalhe.as_view(), name='detalhe'),
    
] 