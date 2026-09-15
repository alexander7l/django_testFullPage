from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='private_index'), # La pagina de la app privada
]