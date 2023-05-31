#from django.db import models
from django.db import models
from ckeditor.fields import RichTextField  


# Create your models here.


class Frase(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    frase = RichTextField()
    imagen = models.ImageField(upload_to='media/', null=True, blank=True)
    privado = models.BooleanField()

    def str(self):
        return f'Soy {self.nombre}, tengo {self.edad} y yo digo que {self.frase}'

class Aviso(models.Model):
    titulo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=600)
 

    def str(self):
        return f'Soy {self.titulo} {self.descripcion}'


