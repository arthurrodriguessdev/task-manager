from django.db import models
from django.contrib.auth.models import User

class Tarefas(models.Model):
    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS = [
        ('nao_iniciada', 'Não iniciada'),
        ('em_andamento', 'Em andamento'),
        ('concluida', 'Concluída'),
    ]

    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    prazo = models.DateField(null=True, blank=True)
    prioridade = models.CharField(choices=PRIORIDADES, null=True, blank=True, default='media')
    status = models.CharField(choices=STATUS, default='nao_iniciada')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
