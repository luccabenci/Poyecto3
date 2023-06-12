from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('insertar/', views.insertar_datos, name='insertar_datos'),
    path('buscar/', views.buscar_datos, name='buscar_datos'),
    path('admin/', admin.site.urls),
]