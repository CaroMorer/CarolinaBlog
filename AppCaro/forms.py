from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)
    last_name: forms.CharField()
    first_name: forms.CharField()    

    class Meta:
        model = User                                             
        fields = ['username','email', 'password1', 'password2', 'last_name', 'first_name' ]
        help_texts= {k:"" for k in fields}
 


class UserEditForm(UserCreationForm): 

    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'username', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}
