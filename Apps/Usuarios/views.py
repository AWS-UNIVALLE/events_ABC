<<<<<<< HEAD
from django.shortcuts import render, redirect
from Apps.Usuarios.forms import UsuarioForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from Apps.Usuarios.models import Usuario
from Apps.Eventos.models import Evento
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
    
    
class crearUsuario(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario_crearusuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
    
def agregarUsuario(request):
    if request.method == "POST":
        usuario_form = UsuarioForm(request.POST)
        
        if usuario_form.is_valid:
            try:
                form = usuario_form.save()
                form.set_password(usuario_form.cleaned_data['password'])
                form.save()
                
                return render_to_response("formulario_crearusuario.html", 
                    {'mensaje' : 'Se guardo correctamente'},
                    context_instance = RequestContext(request))
            except:
                return render_to_response("formulario_crearusuario.html", 
                    locals(),
                    context_instance = RequestContext(request))

    else:
        usuario_form = UsuarioForm()
            
    return render_to_response("formulario_crearusuario.html", locals(), context_instance = RequestContext(request))
    
    
class listarUsuarios(ListView):
    model = Usuario
    template_name = 'listarUsuarios.html'
    
class listareventos(ListView):
    model = Evento
    template_name = 'inicioLogin.html'
    
def index(request):
    return render(request, 'index.html')
    
#def inicio(request):
  #  return render(request, 'inicioLogin.html')
    
    
class modificarUsuario(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'formulario_crearusuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
    
class eliminarUsuario(DeleteView):
    model = Usuario
    template_name = 'eliminarUsuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')
    
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> cd4db6f2812262459b7c57e12642e558c96722cb
