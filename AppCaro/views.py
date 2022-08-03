from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCaro.models import Contacto, DatosPersonales, Habilidades, Idiomas, Profesion, Experiencia
from AppCaro.forms import experiencia_formulario, contacto_formulario, datos_personales_formulario, habilidades_formulario, idiomas_formulario
# Create your views here.

def inicio(request):
    return render(request, 'AppCaro/inicio.html')

def experiencia(request):
    return render(request, 'AppCaro/experiencia.html')

def habilidades(request):
    return render(request, 'AppCaro/habiliadades.html')

def profesion(request):
    return render(request, 'AppCaro/profesion.html')

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

def habilidades(request):

    if request.method == 'POST':

        mi_formulario = habilidades_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            habilidaes = Habilidades (nombre_habilidad = informacion['nombre_habilidad'], descripcion_habilidad = informacion ['descripcion_habilidad'])
            
            habilidades.save()

            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = habilidades_formulario()

    return render(request, 'AppCaro/habilidades.html', {'mi_formulario': mi_formulario })

def idiomas(request):

    if request.method == 'POST':

        mi_formulario = idiomas_formulario(request.POST) 

        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data

            idiomas = Idiomas (primer_idioma = informacion['primer_idioma'], segundo_idioma = informacion ['segundo_idioma'], tercer_idioma =informacion ['tercer_idioma'], lugar = informacion ['lugar'] , fecha = ['fecha'])
            
            idiomas.save()

            return render(request, 'AppCaro/inicio.html')

    else:

        mi_formulario = idiomas_formulario()

    return render(request, 'AppCaro/idiomas.html', {'mi_formulario': mi_formulario })



def buscar_experiencia(request):

    if request.GET['nombre_experiencia']:

        nombre_experiencia = request.GET['nombre_experiencia']
        experiencia = Experiencia.objects.filter(nombre_experiencia__icontains= nombre_experiencia)
        return render(request, 'AppCaro/inicio.html', {'nombre_experiencia':nombre_experiencia} ) 
    else:
        respuesta = 'No ingresaste datos'

    return render(request, 'AppCaro/inicio.html', {'respuesta':respuesta})
