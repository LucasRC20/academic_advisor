from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def formulariop(request):
    return render(request, 'core/formulariop.html')

def sede(request):
    return render(request, 'core/sede.html')

def carrera(request):
    return render(request, 'core/carrera.html')

def alumnos(request):
    return render(request, 'core/alumnos.html')

def entrevistas(request):
    return render(request, 'core/entrevistas.html')