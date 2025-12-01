from rest_framework import viewsets
from .models import Projeto, Tarefa
from .serializers import ProjetoSerializer, TarefaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProjetoViewSet(viewsets.ModelViewSet):
    
    queryset = Projeto.objects.all()
    
    serializer_class = ProjetoSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    
    queryset = Tarefa.objects.all()
    
    serializer_class = TarefaSerializer
    
    
    filter_backends = [DjangoFilterBackend]
    
    
    filterset_fields = ['projeto', 'status', 'prioridade']