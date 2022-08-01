from rest_framework import serializers
from api.models.proprietario import Proprietario

class ProprietarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proprietario
        fields = '__all__'
