from django.shortcuts import render
from django.http import HttpResponse
from steamverde_app.models import Categoria, Pelicula, User, Calificacion, PeliculaCategoria, Comentario

def index(request):
    ultimas_agregadas = Pelicula.objects.all()
    contexto = {
        'ultimas_agregadas' : ultimas_agregadas
    }
    return render(request, "app/index.html", contexto)

def cartelera(request):
    return render(request, "app/cartelera.html")

def categorias(request):
    cat = Categoria.objects.all()
    contexto= {
        'cat' : cat
    }
    return render(request, "app/categories.html", contexto)

def ranking(request):
    return render(request, "app/ranking.html")

def login(request):
    return render(request, "app/login.html")

def register(request):
    return render(request, "app/register.html")

