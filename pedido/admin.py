from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

class ItensInLine(admin.TabularInline):
    model = models.ItemPedido
    extra = 1
    
    
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItensInLine
    ]

admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)