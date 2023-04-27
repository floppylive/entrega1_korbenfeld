from django import forms
from inicio.models import Frase


class CrearFraseFormulario(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    frase= forms.CharField(max_length=450)
    privado=forms.BooleanField(required=False)

    class Meta:
        model = Frase
        fields = ['nombre', 'edad', 'frase', 'privado']

class CrearUsuarioFormulario(forms.Form):
      nombre = forms.CharField(max_length=20)
      apellido = forms.IntegerField()
      inhabilitado=forms.BooleanField( required=False)

class CrearUsuarioFormulario(forms.Form):
        nombre = forms.CharField(max_length=20)
        apellido = forms.CharField(max_length=20)
      #  inhabilitado=forms.BooleanField( required=False)


class CrearModeradorFormulario(forms.Form):
      nombre = forms.CharField(max_length=20)
      apellido = forms.CharField(max_length=20)


class BuscarFrases(forms.Form):
    palabra = forms.CharField(max_length=20)

class BuscarUsuario(forms.Form):
    palabra = forms.CharField(max_length=20, required=False)