from django import forms
from django.forms import ModelForm
from  .models import Vehiculo, Usuario

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']
        
        widget={
            'patente': forms.TextInput(attrs={'class':'form-comtrol'}),
            'marca': forms.TextInput(attrs={'class':'form-comtrol'}),
            'modelo': forms.TextInput(attrs={'class':'form-comtrol'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nomUser','correo','clave','genero','rol']   
        widget={
            'nomUser': forms.TextInput(attrs={'class':'form-comtrol'}),
            'correo': forms.TextInput(attrs={'class':'form-comtrol'}),
            'clave': forms.TextInput(attrs={'class':'form-comtrol'}),
            'genero': forms.Select(attrs={'class':'form-comtrol'}),
            'Rol': forms.Select(attrs={'class':'form-control'}),
        }
    def clean_nomUser(self):
        nomUser = self.cleaned_data.get('nomUser')
        if nomUser.lower() == 'roro':
            raise forms.ValidationError('El nombre de usuario no puede ser "roro".')
        return nomUser