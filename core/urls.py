from django.urls import URLPattern, path
from .views import MenuPrincipal,INICIOSESION,RecuperarContra,form_usuario

urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    path('INICIOSESION',INICIOSESION,name="INICIOSESION"),
    path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    path('form_usuario',form_usuario, name="form_usuario"),
    
]
