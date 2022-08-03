from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCaro.models import Avatar, Contacto, DatosPersonales, Habilidades, Idiomas, Experiencia
from AppCaro.forms import experiencia_formulario, contacto_formulario, datos_personales_formulario, habilidades_formulario, idiomas_formulario, UserRegisterForm, UserCreationForm, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):

      return render(request, "AppCaro/inicio.html")


def experiencia(request):
    return render(request, 'AppCaro/experiencia.html')

def habilidades(request):
    return render(request, 'AppCaro/habiliadades.html')

def idiomas(request):
    return render(request, 'AppCaro/idiomas.html')

@login_required
def experiencia(request):

    if request.method == 'POST':

        mi_formulario = experiencia_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            experiencia = Experiencia (nombre_experiencia = informacion['nombre_experiencia'], nombre_empresa = informacion ['nombre_empresa'], duracion =informacion ['duracion'], trabajo_actual = informacion ['trabajo_actual'] , descripcion = informacion['descripcion'])
            
            experiencia.save()

            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = experiencia_formulario()

    return render(request, 'AppCaro/experiencia.html', {'mi_formulario': mi_formulario })
@login_required
def contacto(request):

    if request.method == 'POST':

        mi_formulario = contacto_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            contacto = Contacto (correo = informacion['correo'], telefono = informacion ['telefono'], instagram =informacion ['instagram'])
            
            contacto.save()

            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = contacto_formulario()

    return render(request, 'AppCaro/contacto.html', {'mi_formulario': mi_formulario })
@login_required
def datos_personales(request):

    if request.method == 'POST':

        mi_formulario = datos_personales_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            datos_personales = DatosPersonales (nombre_y_apellido = informacion['nombre_y_apellido'], edad = informacion ['edad'], dni =informacion ['dni'], domicilio = informacion ['domicilio'] )
            
            datos_personales.save()

            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = datos_personales_formulario()

    return render(request, 'AppCaro/datos_personales.html', {'mi_formulario': mi_formulario })
@login_required
def habilidades(request):

    if request.method == 'POST':

        mi_formulario = habilidades_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            habilidades = Habilidades (nombre_habilidad = informacion['nombre_habilidad'], descripcion_habilidad = informacion ['descripcion_habilidad'])
            
            habilidades.save()

            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = habilidades_formulario()

    return render(request, 'AppCaro/habilidades.html', {'mi_formulario': mi_formulario })
@login_required
def idiomas(request):

    if request.method == 'POST':

        mi_formulario = idiomas_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            idiomas = Idiomas(primer_idioma = informacion['primer_idioma'], segundo_idioma = informacion ['segundo_idioma'], tercer_idioma =informacion ['tercer_idioma'], lugar = informacion ['lugar'] , fecha = ['fecha'])
            
            idiomas.save()


            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = idiomas_formulario()

    return render(request, 'AppCaro/idiomas.html', {'mi_formulario': mi_formulario })



def buscar_experiencia(request):

    if request.GET['nombre_experiencia']:

        variable = request.GET['nombre_experiencia']
        variables = Experiencia.objects.filter(id__icontains= variable)
        return render(request, 'AppCaro/inicio.html', {'variables':variables, 'variable': variable} ) 
    else:
        respuesta = 'No ingresaste datos'

    return render(request, 'AppCaro/inicio.html', {'respuesta':respuesta})

class ExperienciaList(ListView):

    model = Experiencia
    template_name = "AppCaro/experiencia_list.html"

class ExperienciaDetalle(DetailView):

    model = Experiencia
    template_name = "AppCaro/experiencia_detalle.html"

class ExperienciaCrear(LoginRequiredMixin, CreateView):

    model = Experiencia
    success_url = "/AppCaro/experiencia/list"
    fields = ['nombre_experiencia', 'nombre_empresa', 'duracion', 'trabajo_actual', 'descripcion']

class ExperienciaUpdate(UpdateView):

    model = Experiencia
    success_url = "/AppCaro/experiencia/list"
    fields = ['nombre_experiencia', 'nombre_empresa', 'duracion', 'trabajo_actual', 'descripcion']

class ExperienciaDelete(LoginRequiredMixin, DeleteView):

    model = Experiencia
    success_url= "/AppCaro/experiencia/list"

class ContactoList(ListView):
    
    model = Contacto
    template_name= "AppCaro/contacto_list.html"

class ContactoDetalle(DetailView):

    model = Contacto
    template_name = "AppCaro/contacto_detalle.html"

class ContactoCrear(LoginRequiredMixin, CreateView):

    model = Contacto
    success_url = "/AppCaro/contacto/list"
    fields = ['correo', 'telefono', 'instagram']

class ContactoUpdate(LoginRequiredMixin, UpdateView):

    model = Contacto
    success_url = "/AppCaro/curso/list"
    fields = ['correo', 'telefono', 'instagram']

class ContactoDelete(LoginRequiredMixin, DeleteView):

    model = Contacto
    success_url= "/AppCaro/curso/list"

class DatosList(ListView):

    model = DatosPersonales
    template_name = "AppCaro/datos_list.html"

class DatosDetalle(DetailView):

    model = DatosPersonales
    template_name = "AppCaro/datos_detalle.html"

class DatosCrear(LoginRequiredMixin, CreateView):

    model = DatosPersonales
    success_url = "/AppCaro/datos/list"
    fields = ['nombre_y_apellido', 'edad', 'dni', 'domicilio']

class DatosUpdate(LoginRequiredMixin, UpdateView):

    model = DatosPersonales
    success_url = "/AppCaro/datos/list"
    fields = ['nombre_y_apellido', 'edad', 'dni', 'domicilio']

class DatosDelete(LoginRequiredMixin, DeleteView):

    model = DatosPersonales
    success_url= "/AppCaro/datos/list"


class HabilidadesList(ListView):

    model = Habilidades
    template_name = "AppCaro/habilidades_list.html"

class HabilidadesDetalle(DetailView):

    model = Habilidades
    template_name = "AppCaro/habilidades_detalle.html"

class HabilidadesCrear(LoginRequiredMixin, CreateView):

    model = Habilidades
    success_url = "/AppCaro/habilidades/list"
    fields = ['habilidad', 'descripcion']

class HabilidadesUpdate(LoginRequiredMixin, UpdateView):

    model = Habilidades
    success_url = "/AppCaro/habilidades/list"
    fields = ['habilidad', 'descripcion']

class HabilidadesDelete(LoginRequiredMixin, DeleteView):

    model = Habilidades
    success_url= "/AppCaro/habilidades/list"

class IdiomasList(ListView):

    model = Idiomas
    template_name = "AppCaro/idiomas_list.html"

class IdiomasDetalle(DetailView):

    model = Idiomas
    template_name = "AppCaro/idiomas_detalle.html"

class IdiomasCrear(LoginRequiredMixin, CreateView):

    model = Idiomas
    success_url = "/AppCaro/idiomas/list"
    fields = ['primer_idioma', 'segundo_idioma', 'tercer_idioma', 'lugar', 'fecha']

class IdiomasUpdate(LoginRequiredMixin, UpdateView):

    model = Idiomas
    success_url = "/AppCaro/idiomas/list"
    fields = ['primer_idioma', 'segundo_idioma', 'tercer_idioma', 'lugar', 'fecha']

class IdiomasDelete(LoginRequiredMixin, DeleteView):

    model = Idiomas
    success_url= "/AppCaro/idiomas/list"

def login_request(request):

   if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user =authenticate(username=usuario, password=contra)

            if user is not None:
                login(request,user)

                return render(request, "AppCaro/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                
                return render(request,"AppCaro/inicio.html", {"mensaje": f"Error, datos incorrectos"})

        else:
            return render(request,"AppCaro/inicio.html", {"mensaje": "Error, formulario erroneo"})
    
   form = AuthenticationForm()
   return render(request, "AppCaro/login.html", {'form': form})


def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "AppCaro/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserCreationForm()

      return render(request, "AppCaro/registro.html", {"form": form})



@login_required
def editarPerfil(request):
     
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  

                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "AppCaro/inicio.html") 

      else:
           
            miFormulario = UserEditForm(initial={'email':usuario.email})
      

      return render(request, "AppCaro/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})



