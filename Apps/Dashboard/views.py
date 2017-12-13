from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from Apps.Eventos.models import Evento
from Apps.Eventos.forms import EventoForm
from django.core.urlresolvers import reverse_lazy




def reportes(request):
    return render(request, 'reportes.html')
   
# Create your views here.
