import uuid
from django.core.exceptions import ValidationError
from .models import HistoricoModel
from typing import List

class HistoricoService():


    def find_historic_by_animal_id(self, animal_id:str) -> List[HistoricoModel]:
        return HistoricoModel.objects.filter(animal_id=animal_id)

