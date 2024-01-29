# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.http import HttpResponse
# Create your views here.
    
class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Pagar Pedido")

class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Fechar Pedido")
    
class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Detalhe Pedido")
