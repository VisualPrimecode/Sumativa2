from django.shortcuts import render, redirect
from .forms import CustomUserCreatioForm
#from .models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import QF




# Create your views here.

        
def MenuPrincipal(request):
    
    return render(request,'core/menuPrincipal.html')

import logging
from django.contrib.auth.hashers import check_password,make_password

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





