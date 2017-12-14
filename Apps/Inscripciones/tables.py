import django_tables2 as tables
from Apps.Inscripciones.models import Inscripcion
from Apps.Eventos.models import Evento
from Apps.Usuarios.models import Usuario
from django.utils.safestring import mark_safe
import itertools

class TablaEventosBasica(tables.Table):
    row_number = tables.Column(empty_values=())
    id_evento = tables.Column()
    nombre_evento = tables.Column(empty_values=())
    fecha_evento = tables.Column(empty_values=())
    estado = tables.Column()
    
    def __init__(self, tipo_tabla, *args, **kwargs):
        super(TablaEventosBasica, self).__init__(*args, **kwargs)
        self.counter = itertools.count()
        self.tipo_tabla = tipo_tabla
        
    def render_row_number(self):
        return '%d' % next(self.counter)
        
    def render_nombre_evento(self, record):
        id_evento_funcion = record.id
        evento_asociado = Evento.objects.get(pk = id_evento_funcion)
        return evento_asociado.nombre
        
    def render_fecha_evento(self, record):
        id_evento_funcion = record.id
        evento_asociado = Evento.objects.get(pk = id_evento_funcion)
        return evento_asociado.fechaEvento
    
    def get_estado(tipo_estado):
        
        estado = ''
        
        if(tipo_estado == 0):
            estado = Inscripcion.objects.get(evento = evento_asociado).estado_preinscripcion
        elif(tipo_estado == 1):
            estado = Inscripcion.objects.get(evento = evento_asociado).estado_inscripcion
        elif(tipo_estado == 2):
            estado = Inscripcion.objects.get(evento = evento_asociado).estado_pago
            
        return estado
        
    
    def render_estado(self, record):
        id_evento_funcion = record.id
        evento_asociado = Evento.objects.get(pk = id_evento_funcion)
        
        if(self.tipo_tabla == 0):
            return mark_safe('''<a href=%s>Preinscribirse</a>''' % (record.id))
             
        elif(self.tipo_tabla == 1):
            estado = Inscripcion.objects.get(evento = evento_asociado).estado_preinscripcion
            
            ## Si esta en proceso de preinscripcion
            if(estado == 1):
                estado = "En revision de preinscripcion"
            elif(estado == 2):
                estado = "Preinscrito"
            return mark_safe('''<a href=%s>%s</a>''' % (record.id, estado))
    
        elif(self.tipo_tabla == 2):
            estado = Inscripcion.objects.get(evento = evento_asociado).estado_inscripcion
        
            ## Si esta en proceso de Inscripcion
            if(estado == 0):
                estado = "Inscribirse"
            elif(estado == 1):
                estado = "En revision de inscripcion"
            elif(estado == 2):
                estado = "Confirme su inscripcion"
            elif(estado == 3):
                estado = "Inscrito"
        
            return mark_safe('''<a href=%s>%s</a>''' % (record.id, estado))
            
        elif(self.tipo_tabla == 3):
            
            estado = Inscripcion.objects.get(evento = evento_asociado).estado_pago
        
             ## Si esta en proceso de pago
            if(estado == 0):
                estado = "Pagar"
            elif(estado == 1):
                estado = "En confirmacion de pago"
            elif(estado == 2):
                estado = "Pagado"
            
            return mark_safe('''<a href=%s>%s</a>''' % (record.id, estado))  
            
    
class TablaEventos(TablaEventosBasica):
    def __init__(self, *args, **kwargs):
        super(TablaEventos, self).__init__(0, *args, **kwargs)
        
class TablaPreinscripciones(TablaEventosBasica):
    def __init__(self, *args, **kwargs):
        super(TablaPreinscripciones, self).__init__(1, *args, **kwargs)
    
class TablaInscripciones(TablaEventosBasica):
    def __init__(self, *args, **kwargs):
        super(TablaInscripciones, self).__init__(2, *args, **kwargs)
 
class TablaPagos(TablaEventosBasica):
    def __init__(self, *args, **kwargs):
        super(TablaPagos, self).__init__(3, *args, **kwargs)
   
    
class InscripcionesDataManager():
    
    @staticmethod
    def buscar_informacion(cedula_usuario, tipo_tabla):
        
        usuario = Usuario.objects.get(cedula=cedula_usuario)
        
        # tabla de eventos basica
        if(tipo_tabla == 0):
            inscripciones_a_eventos = Inscripcion.objects.filter(participante = usuario).values('evento')
            eventos_sin_preinscripcion = Evento.objects.exclude(id__in=inscripciones_a_eventos)  
            return eventos_sin_preinscripcion
        elif(tipo_tabla == 1):
            inscripciones_a_eventos = Inscripcion.objects.filter(participante = usuario).values('evento')
            eventos_con_preinscripcion = Evento.objects.filter(id__in=inscripciones_a_eventos)
            return eventos_con_preinscripcion
        elif(tipo_tabla == 2):
            inscripciones_a_eventos = Inscripcion.objects.filter(participante = usuario, estado_preinscripcion = 2).values('evento')
            eventos_con_inscripcion = Evento.objects.filter(id__in=inscripciones_a_eventos)
            return eventos_con_inscripcion
        elif(tipo_tabla == 3):
            inscripciones_a_eventos = Inscripcion.objects.filter(participante = usuario, estado_inscripcion = 3).values('evento')
            eventos_con_posibilidad_de_pago = Evento.objects.filter(id__in=inscripciones_a_eventos)
            return eventos_con_posibilidad_de_pago