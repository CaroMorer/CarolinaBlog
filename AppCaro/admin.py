from django.contrib import admin

# Register your models here.
from django import *

from .models import Contacto, DatosPersonales, Experiencia, Habilidades, Idiomas

admin.site.register(Contacto)

admin.site.register(Habilidades)

admin.site.register(DatosPersonales)

admin.site.register(Idiomas)

admin.site.register(Experiencia)






