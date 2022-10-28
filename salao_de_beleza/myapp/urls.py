from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('salao/', views.salao_home, name='salao'),
    path('cadastro/',views.cadastro,name='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('dolog/',views.dolog, name='dolog'),
    path('login/',views.login,name='login'),
    path('perfil/',views.perfil,name='perfil'),
    path('doupdate/',views.doupdate,name='doupdate'),
    path('comentario/',views.comentario,name='comentario'),
    path('comentario/<int:id>/editar/',views.edit_coment, name='edit_coment'),
]