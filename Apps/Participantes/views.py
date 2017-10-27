from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.auth.models import User
from Apps.Participantes.models import Participante
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from Apps.Participantes.forms import RegistroForm

# Create your views here.
class registroParticipante(CreateView):
    model = Participante
    template_name = "registroParticipante.html"
    form_class = RegistroForm
    success_url = reverse_lazy('usuarios:listar_usuarios')
    

    
    
=======

# Create your views here.
>>>>>>> cd4db6f2812262459b7c57e12642e558c96722cb
