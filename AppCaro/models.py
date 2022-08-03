from django.db import models
from django.forms import CharField, DateField
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class DatosPersonales(models.Model):
    nombre_y_apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    dni=models.IntegerField()
    domicilio=models.CharField(max_length=40)

class Contacto(models.Model):
    correo=models.EmailField()
    telefono=models.IntegerField()
    instagram=models.CharField(max_length=10)

class Experiencia(models.Model):
    nombre_experiencia=models.CharField(max_length=20, default="Some String")
    nombre_empresa=models.CharField(max_length=20)
    duracion=models.DateField()
    trabajo_actual=models.BooleanField()
    descripcion=models.CharField(max_length=140)

class Idiomas(models.Model):
    primer_idioma=models.CharField(max_length=10)
    segundo_idioma=models.CharField(max_length=10)
    tercer_idioma=models.CharField(max_length=10)
    lugar=models.CharField(max_length=20)
    fecha=models.DateField()

class Habilidades(models.Model):
    nombre_habilidad=models.CharField(max_length=20)
    descripcion_habilidad=models.CharField(max_length=140)

class Profesion(models.Model):
    nombre=models.CharField(max_length=30)
    fecha=models.DateField()
    descripcion=models.CharField(max_length=200)




    
# Create your models here.
