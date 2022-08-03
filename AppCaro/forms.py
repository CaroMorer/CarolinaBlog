from django import forms

class experiencia_formulario(forms.Form):
    nombre_experiencia = forms.CharField(max_length=20)
    nombre_empresa = forms.CharField(max_length=20)
    duracion = forms.DateField()
    trabajo_actual = forms.BooleanField()
    descripcion = forms.CharField(max_length=140)

class contacto_formulario(forms.Form):
    correo=forms.EmailField()
    telefono=forms.IntegerField()
    instagram=forms.CharField(max_length=10)

class datos_personales_formulario(forms.Form):
    nombre_y_apellido=forms.CharField(max_length=40)
    edad=forms.IntegerField()
    dni=forms.IntegerField()
    domicilio=forms.CharField(max_length=40)


class habilidades_formulario(forms.Form):
    nombre_habilidad=forms.CharField(max_length=20)
    descripcion_habilidad=forms.CharField(max_length=140)


class idiomas_formulario(forms.Form):
    primer_idioma=forms.CharField(max_length=10)
    segundo_idioma=forms.CharField(max_length=10)
    tercer_idioma=forms.CharField(max_length=10)
    lugar=forms.CharField(max_length=20)
    fecha=forms.DateField()

