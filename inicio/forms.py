from django import forms
from inicio.models import Frase, Aviso


class CrearFraseFormulario(forms.ModelForm):
    class Meta:
        model = Frase
        fields= ['nombre', 'edad', 'frase', 'privado']






class CrearAvisoFormulario(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = ['titulo', 'descripcion']



class BuscarFrases(forms.Form):
    palabra = forms.CharField(max_length=20)

class BuscarUsuario(forms.Form):
    palabra = forms.CharField(max_length=20, required=False)