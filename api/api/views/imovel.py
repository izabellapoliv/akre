from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers.imovel import ImovelSerializer
from api.models.imovel import Imovel

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all().order_by('codigo')
    serializer_class = ImovelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['codigo']
