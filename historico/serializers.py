from .models import HistoricoModel
from rest_framework import serializers
from animal.service import AnimalService

_SERVICE_ANIMAL = AnimalService()

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoModel
        fields = ('id', 'animal_id', 'funcionario', 'tipo', 'descricao')

    def create(self, validated_data):
        animal = _SERVICE_ANIMAL.buscar_animal_por_codigo(validated_data.get('codigo_animal'))
        validated_data['animal_id'] = animal.id
        return super().create(validated_data)