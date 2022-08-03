from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers.inquilino import InquilinoSerializer
from api.models.inquilino import Inquilino

class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all().order_by('nome')
    serializer_class = InquilinoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'documento']
