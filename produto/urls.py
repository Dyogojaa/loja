
from django.urls import include, path

from .views import ListaProdutos, DetalheProduto, AdicionarProduto, RemoverProduto, Carrinho, Finalizar

app_name = 'produto'

urlpatterns = [
    path('',ListaProdutos.as_view(), name='produto_lista'),
    path('<slug>',DetalheProduto.as_view(), name='produto_detalhe'),
    path('adicionarcarrinho/',AdicionarProduto.as_view(), name='produto_adiciona'),
    path('removerCarrinho/',RemoverProduto.as_view(), name='produto_remover'),
    path('Carrinho/',Carrinho.as_view(), name='carrinho'),
    path('Finalizar/',Finalizar.as_view(), name='finalizar'),
    
] 