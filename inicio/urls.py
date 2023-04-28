from django.urls import path
from inicio import views
from inicio.models import Frase, Moderador

app_name = 'inicio'


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-frase/', views.crear_frase, name='crear_frase'),
    path('editar-frase/<int:id>/', views.editar_frase, name='editar_frase'),
    path('about/', views.about, name='about'),
    path('frases/', views.lista_frases, name='lista_frases'),
    path('crear-moderador/', views.crear_moderador, name='crear_moderador'),
    path('lista-moderadores/', views.lista_moderadores, name='lista_moderadores'),
    path('eliminar/<int:id>/', views.eliminar_frase, name='eliminar_frase'),
]