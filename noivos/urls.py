from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('lista_convidados/', views.lista_convidados, name='lista_convidados'),
    path('excluir_presente/<int:id>', views.excluir_presente, name='excluir_presente'),
]
