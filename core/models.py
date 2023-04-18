from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    
    def __str__(self):
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente= models.CharField(primary_key=True, max_length=6,verbose_name='Patente')
    marca= models.CharField(max_length=20,verbose_name='Marca vehiculo')
    modelo= models.CharField(max_length=20, null=True , blank=True ,verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente
    
 
class Rol(models.Model):
    idRol=models.IntegerField(primary_key=True, verbose_name='Id de Rol')
    nomRol= models.CharField(max_length=50, verbose_name='Nombre del Rol')
     
    def __str__(self):
        return self.nomRol

class Genero(models.Model):
    idGenero = models.CharField(max_length=20, primary_key=True)  
    nombre = models.CharField(max_length=20, verbose_name='Nombre del genero')

    def __str__(self):
        return self.nombre 

class Usuario(models.Model):
    nomUser= models.CharField(primary_key=True, max_length=20,verbose_name='Nombre del usuario')
    correo= models.CharField(max_length=50,verbose_name='Correo electronico')
    clave= models.CharField(max_length=20,verbose_name='Clave')
    genero =models.ForeignKey(Genero, on_delete=models.CASCADE) 
    rol=models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomUser

# Función para crear instancias iniciales de Genero y Rol
@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    # Crear instancias de Genero si no existen
    if not Genero.objects.exists():
        generos = [
            Genero(idGenero='M', nombre='Masculino'),
            Genero(idGenero='F', nombre='Femenino'),
            Genero(idGenero='O', nombre='Otros')
        ]
        Genero.objects.bulk_create(generos)

    # Crear instancias de Rol si no existen
    if not Rol.objects.exists():
        roles = [
            Rol(idRol=1, nomRol='Administrador'),
            Rol(idRol=2, nomRol='Usuario')
        ]
        Rol.objects.bulk_create(roles)
