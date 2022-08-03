from django.urls import path
from AppCaro import views
# from CaroBlog.AppCaro.views import ContactoCrear, ContactoDetalle, ContactoUpdate, ContactoDelete, ContactoList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('buscar_experiencia/', views.buscar_experiencia),
    path('inicio', views.inicio, name= 'inicio'),
    path('datos_personales', views.datos_personales, name= 'datos_personales'),
    path('contacto', views.contacto, name= 'contacto'),
    path('experiencia', views.experiencia, name= 'experiencia'),
    path('habilidades', views.habilidades, name= 'habilidades'),
    path('idiomas', views.idiomas, name= 'idiomas'),

    path('experiencia/list', views.ExperienciaList.as_view(), name= 'experiencia/list'),
    path(r'^(?P<pk>\d+)$', views.ExperienciaDetalle.as_view(), name = 'Detalle'),
    path(r'^nuevo$', views.ExperienciaCrear.as_view(), name = 'Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.ExperienciaUpdate.as_view(), name = 'Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.ExperienciaDelete.as_view(), name = 'Borrar'),    

    path('contacto/list', views.ContactoList.as_view(), name= 'Lista'),
    path(r'^(?P<pk>\d+)$', views.ContactoDetalle.as_view(), name = 'Detalle'),
    path(r'^nuevo$', views.ContactoCrear.as_view(), name = 'Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.ContactoUpdate.as_view(), name = 'Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.ContactoDelete.as_view(), name = 'Borrar'),

    path('datos/list', views.DatosList.as_view(), name= 'datos/list'),
    path(r'^(?P<pk>\d+)$', views.DatosDetalle.as_view(), name = 'Detalle'),
    path(r'^nuevo$', views.DatosCrear.as_view(), name = 'Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.DatosUpdate.as_view(), name = 'Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.DatosDelete.as_view(), name = 'Borrar'),

    path('habilidades/list', views.HabilidadesList.as_view(), name = 'habilidades/list'),
    path(r'^(?P<pk>\d+)$', views.HabilidadesDetalle.as_view(), name = 'Detalle'),
    path(r'^nuevo$', views.HabilidadesCrear.as_view(), name = 'Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.HabilidadesUpdate.as_view(), name = 'Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.HabilidadesDelete.as_view(), name = 'Borrar'),  

    path('idiomas/list', views.IdiomasList.as_view(), name= 'idiomas/list'),
    path(r'^(?P<pk>\d+)$', views.IdiomasDetalle.as_view(), name = 'Detalle'),
    path(r'^nuevo$', views.IdiomasCrear.as_view(), name = 'Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.IdiomasUpdate.as_view(), name = 'Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.IdiomasDelete.as_view(), name = 'Borrar'),

    path('login', views.login_request, name = 'login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppCaro/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),


    # path('experiencia_formulario', views.experiencia, name = 'experiencia_formulario')
]    