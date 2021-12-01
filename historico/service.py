import uuid
from django.core.exceptions import ValidationError
from .models import HistoricoModel
from typing import List

class HistoricoService():

    def buscar_todos_historico(self) -> HistoricoModel:
        return HistoricoModel.objects.all()

    def buscar_historico_por_id(self, id:uuid) -> HistoricoModel:
        return HistoricoModel.objects.filter(id=id).first()
    
    def deletar_Historico_por_id(self, id:uuid) -> int:
        return HistoricoModel.objects.filter(id=id).delete()

    def find_historic_by_animal_id(self, animal_id:str) -> List[HistoricoModel]:
        return HistoricoModel.objects.filter(animal_id=animal_id)

