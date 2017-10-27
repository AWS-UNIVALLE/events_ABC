from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from django.shortcuts import render_to_response
from django.template import RequestContext



def pruebita(request):
    
    return render_to_response('plantilla.html', {},
                               context_instance=RequestContext(request)) 
=======
>>>>>>> cd4db6f2812262459b7c57e12642e558c96722cb
