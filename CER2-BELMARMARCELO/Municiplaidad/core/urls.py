from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('',views.primeraVista, name='primeraVista'),
    path('registro/', views.registro, name='registro'),
    path('agregar_objeto/', views.agregar_objeto, name='agregar_objeto'),
    path('historial_objetos/', views.historial_objetos, name='historial_objetos'),
    path('contactos/',views.contactos, name='contactos'),
]