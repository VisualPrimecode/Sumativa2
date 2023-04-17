from django.urls import URLPattern, path
from .views import home, form_vehiculo, form_mod_vehiculo, listar_mod_vehiculo,form_del_vehiculo,MenuPrincipal,INICIOSESION,RecuperarContra

urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('home',home,name="home"),
    path('listar-mod-vehiculo', listar_mod_vehiculo, name="listar_mod_vehiculo"),
    path('form_vehiculo', form_vehiculo, name="form_vehiculo"),
    path('form-mod-vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form-del-vehiculo/<id>',form_del_vehiculo, name="form_del_vehiculo"),
    path('INICIOSESION',INICIOSESION,name="INICIOSESION"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    
]
