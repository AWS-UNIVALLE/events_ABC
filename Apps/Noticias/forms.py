from django import forms
from Apps.Noticias.models import Noticia

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        
        fields = [
            'titulo',
            'fechaNoticia',  
            'contenido',
            'imagen',
        ]
        labels = {
            'titulo' : 'Titulo Noticia',
            'fechaNoticia' : 'Fecha',   
            'contenido' : 'Contenido',
            'imagen' : 'Imagen',

        }
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'fechaNoticia' : forms.SelectDateWidget(),
            'contenido' : forms.Textarea(),
            'imagen' : forms.FileInput(),

        }