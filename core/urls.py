from django.urls import path, include
from .views import MenuPrincipal,registro,RecuperarClave,publicaciones_por_categoria
urlpatterns = [
    path('',MenuPrincipal, name="menuPrincipal"),
    #path('INICIOSESION',INICIOSESION,name="INICIOSESION"),
    #path('RecuperarContra',RecuperarContra,name="RecuperarContra"),
    #path('form_usuario',form_usuario, name="form_usuario"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',registro, name="registro"),
    path('RecuperarClave/',RecuperarClave, name="RecuperarClave"),
    path('publicaciones_por_categoria/<int:categoria_id>/',publicaciones_por_categoria, name="publicaciones_por_categoria"),
    
]
