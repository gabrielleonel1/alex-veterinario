import uuid
from django.shortcuts import redirect, render
from django.contrib import messages
from .service import AnimalService
from .serializers import AnimalSerializer

_SERVICE = AnimalService()


def home_animais(request, id:uuid=None):
    if id is not None:
        _SERVICE.deletar_animal_por_id(id)
    elif request.method == "POST" and id is None:
        serializer = AnimalSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            serializer.save()
    animais = _SERVICE.buscar_todos_animais()
    return render(request, 'home-animais.html', context={"animais":animais})

def home_editar_animal(request, id:uuid):
    animal = _SERVICE.buscar_animal_por_id(id)
    
    if request.method == "GET":
        return render(request, 'home-editar-animal.html', context={"animal":animal})

    serializer = AnimalSerializer(animal, request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer.errors)
    else:
        serializer.save()
        messages.success(request, "Salvo com sucesso")
    return render(request, 'home-editar-animal.html', context={"animal":animal})

def home_cliente_animal(request, id:uuid):
    animais = _SERVICE.find_animals_by_cliente_id(id)
    return render(request, 'animais.html', context={"animais":animais, "cliente_id":id})
    