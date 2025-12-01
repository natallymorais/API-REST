from django.db import models

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
       
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('E', 'Em Andamento'),
        ('C', 'Concluída'),
    )
    PRIORIDADE_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, default='B')
    data_limite = models.DateField(blank=True, null=True)
    
    projeto = models.ForeignKey(
        Projeto, 
        on_delete=models.CASCADE, 
        related_name='tarefas'
    )

    def __str__(self):
        
        return self.titulo

