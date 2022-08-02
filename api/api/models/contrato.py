from django.db import models

from api.models.imovel import Imovel

class Contrato(models.Model):
    codigo = models.CharField(max_length=25, unique=True)
    fk_imovel = models.ForeignKey(
        Imovel,
        on_delete=models.CASCADE
    )
    data_inicio_vigencia = models.DateField()
    data_fim_vigencia = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    valor_segurado = models.DecimalField(max_digits=10, decimal_places=2)
    cotacao_taxa = models.DecimalField(max_digits=5, decimal_places=4)

    valor_premio_liquido = models.DecimalField(max_digits=10, decimal_places=2)
    cotacao_iof_total = models.DecimalField(max_digits=5, decimal_places=2)
    valor_premio_total = models.DecimalField(max_digits=10, decimal_places=2)

    possui_seguro_conteudo = models.BooleanField(default=False)
    possui_resp_civil = models.BooleanField(default=False)
    possui_danos_eletricos = models.BooleanField(default=False)
    possui_seguro_vendaval = models.BooleanField(default=False)
    possui_assistencia = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.codigo
