from rest_framework import serializers
from api.models.contrato import Contrato

class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'
