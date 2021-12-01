from django.shortcuts import render

from historico.service import HistoricoService

_SERVICE = HistoricoService()

def home_historico(request, id):
    historico = _SERVICE.find_historic_by_animal_id(id)
    return render(request, 'home-historicos.html', context={"historico":historico, "animal_id":id})