from django.urls import path
from .views import formulariop, home, login, formulariop, sede, carrera

urlpatterns = [
    path('', login, name="login"),
    path('home/', home, name="home"),
    path('formulariop/', formulariop, name="formulariop"),
    path('sede/', sede, name="sede"),
    path('carrera/', carrera, name="carrera"),
]