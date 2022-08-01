from rest_framework import serializers
from api.models.inquilino import Inquilino

class InquilinoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Inquilino
        fields = '__all__'
