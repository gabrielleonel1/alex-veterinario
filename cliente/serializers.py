from .models import ClienteModel
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteModel
        fields = ('id', 'nome', 'cpf', 'sexo', 'telefone', 'email')
