from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Noticias.views import *
#from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', listarNoticias.as_view()),
    url(r'^crearnoticia$', crearNoticia.as_view(), name='crear_noticia'),
    url(r'^listarnoticias', listarNoticias.as_view(), name='listar_noticias'),
    url(r'^modificarnoticia/(?P<pk>\d+)/$', modificarNoticia.as_view(), name='modificar_noticia'),
    url(r'^eliminarnoticia/(?P<pk>\d+)/$', eliminarNoticia.as_view(), name='eliminar_noticia'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)