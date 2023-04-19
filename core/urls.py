from django.urls import URLPattern, path
from .views import home, form_vehiculo, form_mod_vehiculo, listar_mod_vehiculo,form_del_vehiculo,MenuPrincipal,INICIOSESION,RecuperarContra,registro,form_usuario

urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('INICIOSESION',INICIOSESION,name="INICIOSESION"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    path('form_usuario',form_usuario, name="form_usuario"),
    
]
