from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Apps.Inscripciones.views import *
#from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)