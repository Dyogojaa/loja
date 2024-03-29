from collections.abc import Iterable
from django.db import models
from utils import imagens, utils
from django.utils.text import slugify
# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo= models.CharField(
        default ='V',
        max_length=1,
        choices = (
            ('V', 'Variavel'),
            ('S', 'Simples')
        )
    )
    
    def get_preco_formatado(self):        
        return utils.formata_preco(self.preco_marketing)    
    get_preco_formatado.short_description ='Preço'
    
    def get_preco_promo(self):
        return utils.formata_preco(self.preco_marketing_promocional)    
    get_preco_promo.short_description ='Preço Promo'
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            slug =  f'{slugify(self.nome)}'
            self.slug = slug

        
        super().save(*args, **kwargs)
    
        max_image_size = 800

        if self.imagem:
            imagens.resize_image(self.imagem, max_image_size)
         
    
    def __str__(self) -> str:
        return self.nome

class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'