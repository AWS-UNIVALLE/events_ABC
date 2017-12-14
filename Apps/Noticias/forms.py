from django import forms
from Apps.Noticias.models import Noticia

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        
        fields = [
            'titulo',
            'fechaNoticia',  
            'contenido',

        ]
        labels = {
            'titulo' : 'Titulo Noticia',
            'fechaNoticia' : 'Fecha',   
            'contenido' : 'Contenido',

        }
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requerido. 100 Caracteres maximo.'}),
            'fechaNoticia' : forms.SelectDateWidget(),
            'contenido' : forms.Textarea(),

        }