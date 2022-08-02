from rest_framework import viewsets
from rest_framework.response import Response

from calculations.helpers.conteudo_segurado import calculate_total
from calculations.helpers.premio_liquido import calculate_premio_liquido


class PremioLiquidoViewSet(viewsets.ViewSet):
    def create(self, request):
        conteudo_segurado = calculate_total(request.data.get('cotacao_taxa'), request.data.get('valor_segurado'))
        result = calculate_premio_liquido(conteudo_segurado, request.data.get('valor_assistencia'), request.data.get('valor_seguro_vendaval'), request.data.get('valor_resp_civil'), request.data.get('valor_danos_eletricos'))
        return Response({
            'value': result
        })
