from django.shortcuts import render
from django.shortcuts import get_object_or_404
from tarefas.forms import TarefaForm
from tarefas.models import Tarefas


def criar_nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)

        if form.is_valid():
            form.save()

    form = TarefaForm()
    contexto = {
        'form': form
    }

    return render(request, 'base.html', contexto)

def listar_tarefas(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'listar_tarefas.html', {'tarefas': tarefas})

def deletar_tarefa(request, pk):
    tarefa_deletar = get_object_or_404(Tarefas, pk=pk)

    if request.method == 'POST':
        tarefa_deletar.delete()

    contexto = {'tarefa': tarefa_deletar}
    return render(request, 'deletar_tarefa.html', contexto)

def detalhar_tarefa(request, pk):
    tarefa_detalhar = get_object_or_404(Tarefas, pk=pk)
    contexto = {'tarefa': tarefa_detalhar}

    return render(request, 'detalhar_tarefa.html', contexto)

def editar_tarefa(request, pk):
    tarefa_editar = get_object_or_404(Tarefas, pk=pk)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa_editar)

        if form.is_valid():
            form.save()

    form = TarefaForm(instance=tarefa_editar)
    contexto = {'form': form}
    
    return render(request, 'editar_tarefa.html', contexto)

