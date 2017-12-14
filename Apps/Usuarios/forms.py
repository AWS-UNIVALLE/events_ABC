from django import forms
from Apps.Usuarios.models import Usuario


class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        
        CHOICES = (('Administrador', 'Administrador'),('Gerente', 'Gerente'),('Operador', 'Operador'),)
        
        fields = [
            'username',
            'first_name',
            'last_name',
            'email', 
            'password',
            'cedula',
            'telefono',
            'telefono_celular',
            'cargo',

        ]
        labels = {
            'username' : 'User Name',
            'first_name' : 'Nombre',
            'last_name' : 'Apellidos',    
            'email' : 'Correo Electronico',
            'password' : 'Contrasena',
            'cedula' : 'Cedula',
            'telefono' : 'Telefono',
            'telefono_celular': 'Celular',
            'cargo' : 'Cargo',

        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requerido. 100 Caracteres. Solo letras'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requerido. 100 Caracteres. Solo letras'}),
            'cedula' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requerido. 20 Caracteres. Letras y numeros'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Requerido. Ingrese correo valido'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Requerido. 30 Caracteres.'}),
            'telefono_celular': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Requerido. 30 Caracteres'}),
            'cargo' : forms.Select(choices=CHOICES, attrs={'class':'form-control'}),

        }