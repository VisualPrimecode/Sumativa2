from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.
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
    clave= models.CharField(max_length=20,default='clave',verbose_name='Clave')
    genero =models.ForeignKey(Genero, on_delete=models.CASCADE) 
    rol=models.ForeignKey(Rol, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomUser
