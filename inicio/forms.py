from django import forms
from inicio.models import Frase, Aviso


class CrearFraseFormulario(forms.ModelForm):
    #id = forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model = Frase
        fields= ['nombre', 'edad', 'frase', 'privado']
    #nombre = forms.CharField(max_length=20)
   # edad = forms.IntegerField()
   # frase= forms.CharField(max_length=450)
   # privado=forms.BooleanField(required=False)





class CrearAvisoFormulario(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ['titulo', 'descripcion']
      #nombre = forms.CharField(max_length=20)
      #apellido = forms.CharField(max_length=20)


class BuscarFrases(forms.Form):
    palabra = forms.CharField(max_length=20)

class BuscarUsuario(forms.Form):
    palabra = forms.CharField(max_length=20, required=False)