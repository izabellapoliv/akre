from django.db import models

class Imovel(models.Model):
    codigo = models.CharField(max_length=25, unique=True)
    endereco_cep = models.CharField(max_length=8)
    endereco_rua = models.CharField(max_length=255)
    endereco_numero = models.CharField(max_length=5)
    endereco_bairro = models.CharField(max_length=255)
    endereco_cidade = models.CharField(max_length=255)
    endereco_uf = models.CharField(max_length=2)
    endereco_complemento = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
