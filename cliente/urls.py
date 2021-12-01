from django.urls import path
from .views import home, home_cliente, home_editar_cliente


namespace = 'clientes'


urlpatterns = [
path('', home, name="home"),
path('cliente/<uuid:id>/', home_cliente, name="deletar_cliente"),
path('cliente/', home_cliente, name="home_cliente"),
path('cliente/editar/<uuid:id>/', home_editar_cliente, name="home_editar_cliente"),
]