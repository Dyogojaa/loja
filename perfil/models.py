from django.db import models
from django.contrib.auth.models import User
from utils.validacpf import valida_cpf
from django.forms import ValidationError
import re

class Perfil(models.Model):    
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE, verbose_name ='Usuário')
    idade = models.PositiveIntegerField()
    data_nascimento =  models.DateField()
    cpf  = models.CharField(max_length=11)  
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        default ='SP',
        max_length = 2,
        choices =(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )
    
    def __str__(self) -> str:
        return f'{self.usuario}'
    
    def clean(self):
        error_message = {}

        if not valida_cpf(self.cpf):
            error_message['cpf'] = 'Digite um CPF Válido'

        if len(self.cep) != 8 or re.search(r'[^0-9]', self.cep):
            error_message['cep'] = 'Digite apenas números para o CEP e certifique-se de que tem 8 dígitos'

        if error_message:
            raise ValidationError(error_message)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'        
