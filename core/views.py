from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario
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



def INICIOSESION(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(nomUser=username)
            password_usuario = usuario.clave
            user = authenticate(request, username=username, password=password)          
            messages.success(request, '¡Credenciales validadas!')
            login(request, user)
            return redirect('menuPrincipal')
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe')
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'core/INICIOSESION.html', context)



def RecuperarContra(request):
     return render(request,'core/RecuperarContra.html')
def registro(request):
    return render(request,'core/registro.html')

from django.core.exceptions import ValidationError

def form_usuario(request):
    context = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('nomUser')
            correo = formulario.cleaned_data.get('correo')
            if Usuario.objects.filter(Q(nomUser=username) | Q(correo=correo)).exists():
                context['mensaje'] = f"El usuario o correo electrónico ya existe."
            else:
                try:
                    usuario = formulario.save(commit=False)
                    usuario.save()
                    context['mensaje'] = "Guardado correctamente"
                except ValidationError as e:
                    formulario.add_error(None, e)
        else:
            context['form'] = formulario

    return render(request, 'core/form_usuario.html', context)






