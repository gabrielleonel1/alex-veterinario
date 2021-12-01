import uuid
from .models import ClienteModel

class ClienteService():

    def buscar_todos_clientes(self) -> ClienteModel:
        return ClienteModel.objects.all()

    def buscar_cliente_por_id(self, id:uuid) -> ClienteModel:
        return ClienteModel.objects.filter(id=id).first()

    def buscar_cliente_por_cpf(self, cpf:str) -> ClienteModel:
        return ClienteModel.objects.filter(cpf=cpf).first()

    def deletar_cliente_por_id(self, id:uuid) -> int:
        return ClienteModel.objects.filter(id=id).delete()