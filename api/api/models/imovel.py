from django.db import models

from api.models.inquilino import Inquilino
from api.models.proprietario import Proprietario

class Imovel(models.Model):
    codigo = models.CharField(max_length=25, unique=True)
    endereco_cep = models.CharField(max_length=8)
    endereco_rua = models.CharField(max_length=255)
    endereco_numero = models.CharField(max_length=5)
    endereco_bairro = models.CharField(max_length=255)
    endereco_cidade = models.CharField(max_length=255)
    endereco_uf = models.CharField(max_length=2)
    endereco_complemento = models.CharField(max_length=255, null=True, blank=True)

    fk_inquilino = models.ForeignKey(
        Inquilino,
        on_delete=models.CASCADE
    )
    fk_proprietario = models.ForeignKey(
        Proprietario,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.codigo
