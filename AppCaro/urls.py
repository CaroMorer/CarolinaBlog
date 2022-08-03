from django.urls import path
from AppCaro import views


urlpatterns = [
    path('buscar_experiencia/', views.buscar_experiencia),
    path('inicio', views.inicio, name= 'inicio'),
    path('datos_personales', views.datos_personales, name= 'datos_personales'),
    path('contacto', views.contacto, name= 'contacto'),
    path('experiencia', views.experiencia, name= 'experiencia'),
    path('habilidades', views.habilidades, name= 'habilidades'),
    path('idiomas', views.idiomas, name= 'idiomas'),
    path('profesion', views.profesion, name= 'profesion'),
    # path('experiencia_formulario', views.experiencia, name = 'experiencia_formulario')
]    