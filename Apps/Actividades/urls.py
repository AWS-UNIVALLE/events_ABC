
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Actividades.views import *
#from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', listarActividades.as_view()),
    url(r'^crearactividad', crearActividad.as_view(), name='crear_actividad'),
    url(r'^listaractividades', listarActividades.as_view(), name='listar_actividades'),
     url(r'^modificaractividad/(?P<pk>\d+)/$', modificarActividad.as_view(), name='modificar_actividad'),
    url(r'^eliminaractividad/(?P<pk>\d+)/$', eliminarActividad.as_view(), name='eliminar_actividad'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)