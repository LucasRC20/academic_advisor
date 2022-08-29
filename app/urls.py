from django.urls import path
from .views import formulariop, home, login, formulariop, sede, carrera, alumnos, entrevistas

urlpatterns = [
    path('', login, name="login"),
    path('home', home, name="home"),
    path('formulariop', formulariop, name="formulariop"),
    path('sede', sede, name="sede"),
    path('carrera', carrera, name="carrera"),
    path('alumnos', alumnos, name="alumnos"),
    path('entrevistas', entrevistas, name="entrevistas"),
]