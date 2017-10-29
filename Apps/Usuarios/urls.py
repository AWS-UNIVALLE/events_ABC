
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Usuarios.views import *
from Apps.Usuarios.views import listarUsuarios
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    #url(r'^crearusuario', login_required(crearUsuario.as_view()), name='crear_usuario'),
    url(r'^listarusuarios', login_required(listarUsuarios.as_view()), name='listar_usuarios'),
    url(r'^modificarusuario/(?P<pk>\d+)/$', login_required(modificarUsuario.as_view()), name='modificar_usuario'),
    url(r'^eliminarusuario/(?P<pk>\d+)/$', login_required(eliminarUsuario.as_view()), name='eliminar_usuario'),
    url(r'^inicio/', login_required(listareventos.as_view()), name='iniciow'),

    url(r'^crearusuario', login_required(agregarUsuario), name='crear_usuario'),
    


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)