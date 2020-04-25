from django.urls import path 
from . import views 

app_name = 'steamverde_app' 
urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path("cartelera.html", views.cartelera),
    path("categories.html", views.categorias),
    path("ranking.html", views.ranking),
    path("login.html", views.login),
    path("register.html", views.register)
]