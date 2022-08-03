from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers.imovel import ImovelSerializer
from api.models.imovel import Imovel

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all().order_by('codigo')
    serializer_class = ImovelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['codigo', 'tipo', 'fk_inquilino', 'fk_proprietario']
    search_fields = ['endereco_cep', 'endereco_rua', 'endereco_numero', 'endereco_bairro', 'endereco_cidade', 'endereco_uf', 'endereco_complemento']
