from django.shortcuts import render, redirect
from .forms import CustomUserCreatioForm
#from .models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q




# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        
def MenuPrincipal(request):
    
    return render(request,'core/menuPrincipal.html')

import logging
from django.contrib.auth.hashers import check_password,make_password

def RecuperarContra(request):
     return render(request,'core/RecuperarContra.html')
def registro(request):
    return render(request,'core/registro.html')
def RecuperarClave(request):
    return render(request,'core/RecuperarClave.html')

from django.core.exceptions import ValidationError

from django.shortcuts import render, get_object_or_404
from .models import Categoria, Publicacion

def publicaciones_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    publicaciones = Publicacion.objects.filter(categoria=categoria).order_by('-fecha_creacion')
    return render(request, 'foro/publicaciones_por_categoria.html', {'categoria': categoria, 'publicaciones': publicaciones})
def Categoria(request):
    return render(request)
def Publiacion(request):
    return render (request)
def registro(request):
    data={
        'form':CustomUserCreatioForm()
    }
    if request.method=='POST':
        formulario = CustomUserCreatioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"te has registrado correctamente")
            return redirect('menuPrincipal')
        data["form"]=formulario
    return render(request, 'registration/registro.html',data)





