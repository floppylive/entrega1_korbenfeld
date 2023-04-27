from django import forms


class CrearFraseFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    frase= forms.CharField(max_length=450)
    privado=forms.BooleanField( required=False)

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