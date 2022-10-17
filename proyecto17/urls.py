"""proyecto17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from App1.views import saludo, calculo_edad, mostrar_mi_template
#from App1.views import calculo_edad
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/saludar', saludo),
    path('hola-mundo/calcular_edad/<a_nac>', calculo_edad),
    path('hola-mundo/responder_con_template/', mostrar_mi_template),
]
