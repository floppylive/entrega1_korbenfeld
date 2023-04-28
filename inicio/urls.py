from django.urls import path
from inicio import views


app_name = 'inicio'


urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-frase/', views.crear_frase, name='crear_frase'),
    path('editar-frase/<int:id>/', views.editar_frase, name='editar_frase'),
    path('editar-aviso/<int:id>/', views.editar_aviso, name='editar_aviso'),
    path('about/', views.about, name='about'),
    path('frases/', views.lista_frases, name='lista_frases'),
    path('crear-aviso/', views.crear_aviso, name='crear_aviso'),
    path('lista-avisos/', views.lista_avisos, name='lista_avisos'),
    path('eliminar/<int:id>/', views.eliminar_frase, name='eliminar_frase'),
    path('eliminar-aviso/<int:id>/', views.eliminar_aviso, name='eliminar_aviso'),
]