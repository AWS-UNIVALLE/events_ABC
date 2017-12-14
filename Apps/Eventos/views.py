from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from Apps.Eventos.models import Evento
from Apps.Eventos.forms import EventoForm
from django.core.urlresolvers import reverse_lazy
# Create your views here.

    
class crearEvento(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'formulario_crearevento1.html'
    success_url = reverse_lazy('eventos:listar_eventos')
    
class listarEventos(ListView):
    model = Evento
    template_name = 'listarEventos.html'
    
class modificarEvento(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'formulario_crearevento1.html'
    success_url = reverse_lazy('eventos:listar_eventos')
    
class eliminarEvento(DeleteView):
    model = Evento
    template_name = 'eliminarEvento.html'
    success_url = reverse_lazy('eventos:listar_eventos')
    
class verEvento(ListView):
    model = Evento
    template_name = 'unEvento.html'
# Create your views here.
