from rest_framework import viewsets
from rest_framework.response import Response

from calculations.helpers.conteudo_segurado import calculate_total


class ConteudoSeguradoViewSet(viewsets.ViewSet):
    def create(self, request):
        result = calculate_total(request.data.get('cotacao_taxa'), request.data.get('valor_segurado'))
        return Response({
            'value': result
        })
