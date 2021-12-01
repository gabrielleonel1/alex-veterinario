from typing import List
import uuid
from .models import AnimalModel

class AnimalService():

    def buscar_todos_animais(self) -> AnimalModel:
        return AnimalModel.objects.all()

    def buscar_animal_por_id(self, id:uuid) -> AnimalModel:
        return AnimalModel.objects.filter(id=id).first()
    
    def deletar_animal_por_id(self, id:uuid) -> int:
        return AnimalModel.objects.filter(id=id).delete()

    def find_animals_by_cliente_id(self, cliente_id:str) -> List[AnimalModel]:
        return AnimalModel.objects.filter(cliente_id=cliente_id)
