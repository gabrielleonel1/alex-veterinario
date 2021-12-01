from .models import AnimalModel
from rest_framework import serializers

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalModel
        fields = ('id', 'cliente_id', 'nome', 'raca', 'sexo', 'idade',)