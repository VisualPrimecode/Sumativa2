from django import forms
from django.forms import ModelForm
from  .models import Vehiculo

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
        
       