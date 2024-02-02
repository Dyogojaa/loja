
from django.urls import include, path

from .views import ListaProdutos, DetalheProduto, AdicionarCarrinho, RemoverCarrinho, Carrinho, Finalizar

app_name = 'produto'

urlpatterns = [
    path('',ListaProdutos.as_view(), name='lista'),
    path('<slug>',DetalheProduto.as_view(), name='detalhe'),
    path('adicionarcarrinho/',AdicionarCarrinho.as_view(), name='adicionarcarrinho'),
    path('removercarrinho/',RemoverCarrinho.as_view(), name='removercarrinho'),
    path('carrinho/',Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/',Finalizar.as_view(), name='resumodacompra'),
    
] 