from django.shortcuts import render
from django_tables2 import views
from django_tables2 import SingleTableView
from django_tables2 import SingleTableMixin
from Apps.Inscripciones.models import Inscripcion
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django_tables2 import RequestConfig

from Apps.Inscripciones.models import Inscripcion
from Apps.Inscripciones.tables import TablaEventosBasica, InscripcionesDataManager
from Apps.Inscripciones.tables import TablaEventos, TablaPreinscripciones, TablaInscripciones, TablaPagos

def index(request):
    datos_tabla_eventos = InscripcionesDataManager.buscar_informacion('1144198691', 0)
    tabla_eventos = TablaEventos(datos_tabla_eventos)
    
    datos_tabla_preinscripciones = InscripcionesDataManager.buscar_informacion('1144198691', 1)
    tabla_preinscripciones = TablaPreinscripciones(datos_tabla_preinscripciones)
    
    datos_tabla_inscripciones = InscripcionesDataManager.buscar_informacion('1144198691', 2)
    tabla_inscripciones = TablaInscripciones(datos_tabla_inscripciones)
    
    datos_tabla_pagos = InscripcionesDataManager.buscar_informacion('1144198691', 3)
    tabla_pagos = TablaPagos(datos_tabla_pagos)
    
    RequestConfig(request, paginate=False).configure(tabla_eventos)
    RequestConfig(request, paginate=False).configure(tabla_preinscripciones)
    RequestConfig(request, paginate=False).configure(tabla_inscripciones)
    RequestConfig(request, paginate=False).configure(tabla_pagos)
    
    tablas = {
        'tabla_eventos': tabla_eventos,
        'tabla_preinscripciones': tabla_preinscripciones,
        'tabla_inscripciones': tabla_inscripciones,
        'tabla_pagos': tabla_pagos,
    }
    
    return render(request, 'visualizar_inscripciones.html', tablas)


# Create your views here.
