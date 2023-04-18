from django.shortcuts import render, redirect
from .forms import VehiculoForm,UsuarioForm
from .models import Vehiculo,Usuario
from django.core.exceptions import ValidationError

# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        
def home(request):
    
    vehiculos = Vehiculo.objects.all()
    datos={
        'vehiculos':vehiculos
    }
    
    hijo=persona("Juan Perez","7")
    lista=["Accion","terror","fentinol"]
    contexto={"nombre":"Claudio Andres", "Categorias":lista,"hijo":hijo,"Vehiculos":vehiculos}
    return render(request,'core/home.html',contexto)

def form_vehiculo(request):
    datos={
        'form':VehiculoForm()
    }
    if request.method== 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
    return render(request, 'core/form_vehiculo.html',datos)

def form_mod_vehiculo(request, id):
    auto = Vehiculo.objects.get(patente=id)
    datos ={
        'form': VehiculoForm(instance=auto)
    }
    if request.method== 'POST':
        formulario = VehiculoForm(data=request.POST, instance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
      
    return render(request, 'core/form_mod_vehiculo.html',datos)

def listar_mod_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        "vehiculos":vehiculos
    }
    return render(request, 'core/listar_mod_vehiculo.html',datos)

def form_del_vehiculo(request, id):
    aut = Vehiculo.objects.get(patente=id)
    datos ={
        'form': VehiculoForm(instance=aut)
    }
    if request.method== 'POST':
        formulario = VehiculoForm(data=request.POST, instance=aut)
        aut.delete()
        datos['mensaje'] = "Eliminado correctamente"
      
    return render(request, 'core/form_del_vehiculo.html',datos)
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
     return render(request,'core/INICIOSESION.html')
def RecuperarContra(request):
     return render(request,'core/RecuperarContra.html')
def registro(request):
    return render(request,'core/registro.html')
def form_usuario(request):
    context = {
        'form': UsuarioForm()  # Pasa el formulario al contexto de la plantilla
    }
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            try:
                usuario = formulario.save(commit=False)
                # Realiza cualquier otra operación adicional antes de guardar el modelo
                usuario.save()
                context['mensaje'] = "Guardados correctamente"
            except ValidationError as e:
                # Maneja la excepción de validación personalizada
                formulario.add_error('nomUser', e)  # Agrega el error al formulario
    return render(request, 'core/form_usuario.html', context)
