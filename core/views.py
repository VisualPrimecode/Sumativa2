from django.shortcuts import render, redirect
from .forms import VehiculoForm,UsuarioForm
from .models import Vehiculo,Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib import messages



# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        
def MenuPrincipal(request):
    
    vehiculos = Vehiculo.objects.all()
    datos={
        'vehiculos':vehiculos
    }
    
    hijo=persona("Juan Perez","7")
    lista=["Accion","terror","fentinol"]
    contexto={"nombre":"Claudio Andres", "Categorias":lista,"hijo":hijo,"Vehiculos":vehiculos}
    return render(request,'core/menuPrincipal.html',contexto)

def INICIOSESION(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menuPrincipal')
        else:
            messages.error(request, 'Credenciales inválidas')
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
            try:
                usuario = formulario.save(commit=False)
                
                usuario.save()
                context['mensaje'] = "Guardados correctamente"
            except ValidationError as e:
                
                formulario.add_error(None, e)  
        else:
            
            context['form'] = formulario
    return render(request, 'core/form_usuario.html', context)

