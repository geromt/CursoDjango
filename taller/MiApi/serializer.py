from rest_framework import serializers
from App1.models import AutorModel, FraseModel


class AutorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorModel
        fields = '__all__'


class AutorConFraseSerializer(serializers.ModelSerializer):
    frases = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='frases-detail')
    class Meta:
        model = AutorModel
        fields = '__all__'


class FraseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FraseModel
        fields = '__all__'
