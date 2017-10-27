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
            'cargo' : 'Cargo',

        }
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'cedula' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'cargo' : forms.Select(choices=CHOICES, attrs={'class':'form-control'}),

        }