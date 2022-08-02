from rest_framework import viewsets

from api.serializers.inquilino import InquilinoSerializer
from api.models.inquilino import Inquilino

class InquilinoViewSet(viewsets.ModelViewSet):
    queryset = Inquilino.objects.all().order_by('nome')
    serializer_class = InquilinoSerializer
