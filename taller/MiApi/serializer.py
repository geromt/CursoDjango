from rest_framework import serializers
from App1.models import AutorModel

class AutorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutorModel
        fields = '__all__'
