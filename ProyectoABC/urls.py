"""ProyectoABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Actividades.views import *
#from Apps.Dashboard.views import *
from Apps.Eventos.views import *
from Apps.Noticias.views import *
from Apps.Usuarios.views import *
from django.contrib.auth.views import login, logout_then_login

#from Apps.Participantes.views import *
#from django.contrib.auth.views import login, logout_then_login
#URLS PRINCIPALES


urlpatterns = [
    url(r'^admin/', admin.site.urls),
   
    url(r'^accounts/login/', login, {'template_name':'loginparticipante.html'}, name='login'),
    url(r'^eventos/', include('Apps.Eventos.urls', namespace='eventos')),
    url(r'^actividades/', include('Apps.Actividades.urls', namespace='actividades')),
    url(r'noticias/', include('Apps.Noticias.urls', namespace='noticias')),
    url(r'usuarios/', include('Apps.Usuarios.urls', namespace='usuarios')),
    url(r'participantes/', include('Apps.Participantes.urls', namespace='participantes')),
    url(r'dashboard/', include('Apps.Dashboard.urls', namespace='dashboard')),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

