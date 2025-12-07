from django import forms
from tarefas import models

class TarefaForm(forms.ModelForm):
    class Meta:
        model = models.Tarefas
        fields = ('titulo', 'descricao', 'prazo', 'prioridade', 'status')
