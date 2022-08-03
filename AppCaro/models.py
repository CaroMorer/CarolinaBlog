from django.db import models
from django.forms import CharField, DateField
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class DatosPersonales(models.Model):
    nombre_y_apellido=models.CharField(max_length=40)
    edad=models.IntegerField()
    dni=models.IntegerField()
    domicilio=models.CharField(max_length=40)

    def __str__(self):
        return f"Nombre y Apellido: {self.nombre_y_apellido} - Edad: {self.edad} - DNI: {self.dni} - Domicilio: {self.domicilio}"

class Contacto(models.Model):
    correo=models.EmailField()
    telefono=models.IntegerField()
    instagram=models.CharField(max_length=10)

    def __str__(self):
        return f"Correo:{self.correo} - Telefono:{self.telefono} - Instagram: {self.instagram}"

class Experiencia(models.Model):
    nombre_experiencia=models.CharField(max_length=20)
    nombre_empresa=models.CharField(max_length=20)
    duracion=models.DateField()
    trabajo_actual=models.BooleanField()
    descripcion=models.CharField(max_length=140)

    def __str__(self):
        return f" Cargo: {self.nombre_experiencia} - Empresa: {self.nombre_empresa} - Duracion: {self.duracion} - Trabajo Actual: {self.trabajo_actual} - Descripción: {self.descripcion}"

class Idiomas(models.Model):
    primer_idioma=models.CharField(max_length=10)
    segundo_idioma=models.CharField(max_length=10)
    tercer_idioma=models.CharField(max_length=10)
    lugar=models.CharField(max_length=20)
    fecha=models.DateField()

    def __str__(self):
        return f"Idioma 1:{self.primer_idioma} - Idioma 2: {self.segundo_idioma} - Idioma 3 {self.tercer_idioma} - Lugar {self.lugar} - Fecha {self.fecha}"

class Habilidades(models.Model):
    nombre_habilidad=models.CharField(max_length=20)
    descripcion_habilidad=models.CharField(max_length=140)

    def __str__(self):
        return f"Habilidad:{self.nombre_habilidad} - Descripcion {self.descripcion_habilidad}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)





    
# Create your models here.
