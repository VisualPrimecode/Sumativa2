from django.urls import path, include
from .views import MenuPrincipal,INICIOSESION,RecuperarContra,form_usuario,registro

urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('INICIOSESION',INICIOSESION,name="INICIOSESION"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    path('form_usuario',form_usuario, name="form_usuario"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',registro, name="registro"),
    
]
