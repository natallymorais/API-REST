from django.contrib import admin
from .models import Projeto, Tarefa
from rest_framework.authtoken.models import Token
# Admin para o modelo Autor: mostra o campo 'nome' e permite busca por nome
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data_criacao']         # colunas no admin
    search_fields = ['nome', 'descricao']           # campos pesquisáveis
    list_filter = ['data_criacao']                  # filtros laterais

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'status', 'prioridade', 'data_limite', 'projeto']
    search_fields = ['titulo']                      # pesquisa
    list_filter = ['status', 'prioridade', 'projeto']   # filtros laterais
admin.site.register(Token)