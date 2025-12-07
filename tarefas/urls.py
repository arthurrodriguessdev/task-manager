from django.urls import path
from tarefas import views

urlpatterns = [
    path('adicionar_tarefa', views.criar_nova_tarefa, name='adicionar_tarefa')
]