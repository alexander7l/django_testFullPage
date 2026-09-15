from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),              # Raiz de la app publica
    path('login/', views.login_view, name='login'),   # Pagina del formulario
]