from django.urls import path
from .views import home_animais, home_editar_animal, home_cliente_animal

namespace = 'animais'

urlpatterns = [
    path('animais/', home_animais, name="home_animais"),
    path('animais/<uuid:id>/', home_animais, name="deletar_animal"),
    path('animais/editar/<uuid:id>/', home_editar_animal, name="home_editar_animal"),
    path('animais/cliente/<uuid:id>/', home_cliente_animal, name="home_animal_cliente"),
]