from django.urls import path
from inicio import views
from inicio.models import Frase, Moderador,Usuario

app_name = 'inicio'


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-frase/', views.crear_frase, name='crear_frase'),
    path('editar-frase/', views.editar_frase, name='editar_frase'),
    path('about/', views.about, name='about'),
    path('frases/', views.lista_frases, name='lista_frases'),
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear-moderador/', views.crear_moderador, name='crear_moderador'),

   # path('mostrar-fecha/', views.mostrar_fecha, name='mostrar_fecha'),
  #  path('saludar/<str:nombre>/<str:apellido>/', views.saludar, name='saludar'),
   # path('mi-primer-template/', views.mi_primer_template, name='mi_primer_template'),
   # path('prueba-template/', views.prueba_template, name='prueba_template'),
   # path('crear-animal/', views.crear_animal, name='crear_animal'),
   # path('animales/', views.lista_animales, name='listar_animales'),
   # path('prueba-render/', views.prueba_render, name='prueba_render'),
]

