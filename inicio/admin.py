from django.contrib import admin
from inicio.models import Frase, Moderador


# Register your models here.



# v2
admin.site.register([Frase, Moderador])