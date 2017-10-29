from django.shortcuts import render, redirect
from Apps.Noticias.forms import NoticiaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Apps.Noticias.models import Noticia
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class crearNoticia(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'formulario_crearnoticia.1.html'
    success_url = reverse_lazy('noticias:listar_noticias')
    
class listarNoticias(ListView):
    model = Noticia
    template_name = 'listarNoticias.html'
    
class modificarNoticia(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'formulario_crearnoticia.1.html'
    success_url = reverse_lazy('noticias:listar_noticias')
    
class eliminarNoticia(DeleteView):
    model = Noticia
    template_name = 'eliminarNoticia.html'
    success_url = reverse_lazy('noticias:listar_noticias')