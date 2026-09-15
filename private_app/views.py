from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Se importa la funcion login_required de django

# Create your views here.

# Funcion que renderiza el html de la app privada
# El decorador @ (funcion) se ejecuta antes de index y valida la cookie asignada a ese usuario
@login_required # Esto bloquea el acceso (no bypass)
# Si la cookie es valida se renderiza la app privada
def index(request):
    return render(request, 'private_app/index.html')