from rest_framework import viewsets
from rest_framework.response import Response

from calculations.helpers.importancia_segurada import calculate_importancia_segurada

from calculations.helpers.conteudo_segurado import calculate_total
from calculations.helpers.resp_civil import calculate_cobertura_resp_civil
from calculations.helpers.danos_eletricos import calculate_cobertura_danos_eletricos
from calculations.helpers.cobertura_vendaval import calculate_cobertura_vendaval

from calculations.helpers.premio_liquido import PremioLiquido
from calculations.helpers.iof_total import calculate_iof_total
from calculations.helpers.premio_total import calculate_premio_total


class ContractViewSet(viewsets.ViewSet):
    def create(self, request):
        importancia_segurada = calculate_importancia_segurada(aluguel=request.data.get('aluguel'))
        conteudo_segurado = calculate_total(importancia_segurada=importancia_segurada)
        cobertura_resp_civil = calculate_cobertura_resp_civil()
        cobertura_danos_eletricos = calculate_cobertura_danos_eletricos()
        cobertura_vendaval = calculate_cobertura_vendaval()

        premio_liquido_class = PremioLiquido(aluguel=request.data.get('aluguel'))
        if request.data.get('optionals')['with_seguro_conteudo']:
            premio_liquido_class.with_seguro_conteudo()
        if request.data.get('optionals')['with_resp_civil']:
            premio_liquido_class.with_resp_civil()
        if request.data.get('optionals')['with_danos_eletricos']:
            premio_liquido_class.with_danos_eletricos()
        if request.data.get('optionals')['with_cobertura_vendaval']:
            premio_liquido_class.with_cobertura_vendaval()
        if request.data.get('optionals')['with_assistencia']:
            premio_liquido_class.with_assistencia()

        premio_liquido = premio_liquido_class.calculate()
        iof_total = calculate_iof_total(premio_liquido)
        premio_total = calculate_premio_total(premio_liquido=premio_liquido, iof_total=iof_total)

        return Response({
            'importancia_segurada': importancia_segurada,
            'conteudo_segurado': conteudo_segurado,
            'cobertura_resp_civil': cobertura_resp_civil,
            'cobertura_danos_eletricos': cobertura_danos_eletricos,
            'cobertura_vendaval': cobertura_vendaval,
            'premio_liquido': premio_liquido,
            'iof_total': iof_total,
            'premio_total': premio_total,
        })
