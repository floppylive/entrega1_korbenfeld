from django.contrib import admin
from inicio.models import Frase, Aviso


# Register your models here.



# v2
admin.site.register([Frase, Aviso])