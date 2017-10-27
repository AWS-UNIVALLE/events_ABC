<<<<<<< HEAD
from django.shortcuts import render, redirect
from Apps.Actividades.forms import ActividadForm
from Apps.Actividades.models import Actividad
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
    
class crearActividad(CreateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'formulario_crearactividad.1.html'
    success_url = reverse_lazy('actividades:listar_actividades')
    
class listarActividades(ListView):
    model = Actividad
    template_name = 'listarActividades.html'
    
class modificarActividad(UpdateView):
    model = Actividad
    form_class = ActividadForm
    template_name = 'formulario_crearactividad.1.html'
    success_url = reverse_lazy('actividades:listar_actividades')
    
class eliminarActividad(DeleteView):
    model = Actividad
    template_name = 'eliminarActividad.html'
    success_url = reverse_lazy('actividades:listar_actividades')
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> cd4db6f2812262459b7c57e12642e558c96722cb
