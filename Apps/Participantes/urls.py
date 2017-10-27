from django.conf.urls import url

from Apps.Participantes.views import registroParticipante

urlpatterns = [
    
    url(r'^registrar', registroParticipante.as_view(), name="registrar"),
    
    ]