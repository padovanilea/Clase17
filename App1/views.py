from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
	return HttpResponse("Hola como vai?. Este es un proyecto de la clase 17.")

def calculo_edad(request, a_nac):
    edad = 2022 - int(a_nac)
    #mensaje = "La idea es calcular la edad del usuario, \nquien ingresa por pantalla el año de su nacimiento."
    mensaje = f"Edad = año actual (2022) - año de nacimiento ({a_nac}): {edad} años"
    return HttpResponse(mensaje)

def mostrar_mi_template (request):
    return render(request, "App1/index.html")
