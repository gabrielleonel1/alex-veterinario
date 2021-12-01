from django.shortcuts import render
import uuid
from .service import ClienteService
from .serializers import ClienteSerializer
from django.contrib import messages


_SERVICE = ClienteService()

def home(request):
    return render(request, 'home.html')
    
def home_cliente(request, id:uuid=None):
    if id is not None:
        _SERVICE.deletar_cliente_por_id(id)
    elif request.method == "POST" and id is None:
        serializer = ClienteSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            serializer.save()
    clientes = _SERVICE.buscar_todos_clientes()
    return render(request, 'home-cliente.html', context={"clientes":clientes})

def home_editar_cliente(request, id:uuid):
    cliente = _SERVICE.buscar_cliente_por_id(id)
    
    if request.method == "GET":
        return render(request, 'home-editar-cliente.html', context={"cliente":cliente})

    serializer = ClienteSerializer(cliente, request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer.errors)
    else:
        serializer.save()
        messages.success(request, "Salvo com sucesso")
    return render(request, 'home-editar-cliente.html', context={"cliente":cliente})
