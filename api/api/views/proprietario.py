from rest_framework import viewsets

from api.serializers.proprietario import ProprietarioSerializer
from api.models.proprietario import Proprietario

class ProprietarioViewSet(viewsets.ModelViewSet):
    queryset = Proprietario.objects.all().order_by('nome')
    serializer_class = ProprietarioSerializer
