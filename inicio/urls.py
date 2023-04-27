from django.urls import path
from inicio import views
from inicio.models import Frase, Moderador,Usuario

app_name = 'inicio'


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-frase/', views.crear_frase, name='crear_frase'),
    path('editar-frase/<int:frase_id>/', views.editar_frase, name='editar_frase'),
    path('about/', views.about, name='about'),
    path('frases/', views.lista_frases, name='lista_frases'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear-moderador/', views.crear_moderador, name='crear_moderador'),
]