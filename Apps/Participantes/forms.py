from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Apps.Participantes.models import Participante

class RegistroForm(forms.ModelForm):
    
    class Meta:
        model = Participante
        
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'cedula',
            'password',
            
            ]
        labels = {
            'username' : 'User Name',
            'first_name' : 'Nombre',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',
            'cedula' : 'Numero Cedula',
            'password' : 'Contrasena',

        }
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'cedula' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),

        }