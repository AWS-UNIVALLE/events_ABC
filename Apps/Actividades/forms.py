from django import forms
from Apps.Actividades.models import Actividad

class ActividadForm(forms.ModelForm):
    
    class Meta:
        model = Actividad
        
        fields = [
            'nombre',
            'fechaActividad',  
            'duracion',
            'descripcion',
            'evento',

        ]
        labels = {
            'nombre' : 'Nombre',
            'fechaActividad' : 'Fecha',    
            'duracion' : 'Duracion',
            'descripcion' : 'Descripcion',
            'evento' : 'Evento',

        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'fechaActividad' : forms.SelectDateWidget(),
            'duracion': forms.DateInput(),
            'descripcion' : forms.Textarea(),
            'evento' : forms.Select(attrs={'class':'form-control'}),

        }