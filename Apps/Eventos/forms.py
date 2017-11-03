from django import forms
from Apps.Eventos.models import Evento

class EventoForm(forms.ModelForm):
    
    class Meta:
        model = Evento
        
        CHOICES = (('Activo', 'Activo'),('Inactivo', 'Inactivo'),)

        
        fields = [
            'nombre',
            'fechaEvento',  
            'duracion',
            'estado',
            'descripcion',
        ]
        labels = {
            'nombre' : 'Nombre',
            'fechaEvento' : 'Fecha',    
            'duracion' : 'Duracion',
            'estado' : 'Estado',
            'descripcion' : 'Descripcion',

        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Requerido. 100 Caracteres maximo.'}),
            'fechaEvento' : forms.SelectDateWidget(),
            'duracion': forms.DateInput(),
            'estado': forms.Select(choices=CHOICES, attrs={'class':'form-control'}),
            'descripcion' : forms.Textarea(),

        }