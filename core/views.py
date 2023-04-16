from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo

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