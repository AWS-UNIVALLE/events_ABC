from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Eventos.views import *
#from django.contrib.auth.decorators import login_required
#URLS EVENTOs

urlpatterns = [
    url(r'^$', listarEventos.as_view()),
    url(r'^principal', paginaPrincipal),
    url(r'^crearevento$', crearEvento.as_view(), name='crear_evento'),
    url(r'^listareventos$', listarEventos.as_view(), name='listar_eventos'),
    url(r'^modificarevento/(?P<pk>\d+)/$', modificarEvento.as_view(), name='modificar_evento'),
    url(r'^eliminarevento/(?P<pk>\d+)/$', eliminarEvento.as_view(), name='eliminar_evento'),
    url(r'^verevento/(?P<pk>\d+)/$', verEvento.as_view(), name='ver_evento'),

    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)