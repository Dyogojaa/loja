from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models    


# Create your views here.
class ListaProdutos(ListView):
    model = models.Produto
    template_name = 'produto/lista.html'
    context_object_name = 'produtos'
    paginate_by = 10
    
    
class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'
    

class AdicionarProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Adicionar Produtos")
    
class RemoverProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Remover Produtos")
    
class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Carrinho")
    
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Finalziar")
    