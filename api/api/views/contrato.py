from rest_framework import viewsets

from api.serializers.contrato import ContratoSerializer
from api.models.contrato import Contrato

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all().order_by('codigo')
    serializer_class = ContratoSerializer
