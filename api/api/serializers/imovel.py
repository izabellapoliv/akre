from rest_framework import serializers
from api.models.imovel import Imovel

class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
