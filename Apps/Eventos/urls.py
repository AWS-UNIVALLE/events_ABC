from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Eventos.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(listarEventos.as_view())),
    url(r'^crearevento$', login_required(crearEvento.as_view()), name='crear_evento'),
    url(r'^listareventos$', login_required(listarEventos.as_view()), name='listar_eventos'),
    url(r'^modificarevento/(?P<pk>\d+)/$', login_required(modificarEvento.as_view()), name='modificar_evento'),
    url(r'^eliminarevento/(?P<pk>\d+)/$', login_required(eliminarEvento.as_view()), name='eliminar_evento'),
    
    url(r'^verevento/(?P<pk>\d+)/$', login_required(verEvento.as_view()), name='ver_evento'),

    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)