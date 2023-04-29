from django import forms
from django.forms import ModelForm
from  .models import Usuario
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    ROL_CHOICES = (
        ('A', 'Administrador'),
        ('U', 'Usuario'),
    )
    # Lista de palabras prohibidas
    PALABRAS_PROHIBIDAS = ['badword1', 'badword2']  #no dio tiempo a agregar.s

    class Meta:
        model = Usuario
        fields = ['nomUser', 'correo', 'clave', 'genero', 'rol']
        widgets = {
            'nomUser': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_nomUser(self):
        nomUser = self.cleaned_data.get('nomUser')
        for palabra in self.PALABRAS_PROHIBIDAS:
            if palabra in nomUser.lower():
                raise forms.ValidationError('El nombre de usuario contiene una palabra prohibida.')
        return nomUser

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        try:
            validate_email(correo)
        except forms.ValidationError:
            raise forms.ValidationError('Por favor ingrese un correo válido.')
        return correo
    def clean_clave(self):
        clave = self.cleaned_data.get('clave')
        # Verificar si la contraseña cumple con los requisitos
        if not re.search(r'[A-Z]', clave):
            raise forms.ValidationError('La contraseña debe contener al menos una letra mayúscula.')
        if not re.search(r'[a-z]', clave):
            raise forms.ValidationError('La contraseña debe contener al menos una letra minúscula.')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', clave):
            raise forms.ValidationError('La contraseña debe contener al menos un signo de puntuación.')
        if len(clave) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return clave
class CustomUserCreatioForm(UserCreationForm):
    
    class Meta:
        model = User
        fields= ["username" , "first_name" , "last_name" , "email" , "password1" , "password2"]