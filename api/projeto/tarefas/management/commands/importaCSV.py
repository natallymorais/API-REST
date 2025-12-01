import csv
from django.core.management.base import BaseCommand
from tarefas.models import Projeto, Tarefa

class Command(BaseCommand):
    help = "Importa projetos e tarefas a partir de arquivos CSV"

    def add_arguments(self, parser):
        parser.add_argument('--projetos', type=str, required=True, help='Caminho do arquivo projeto.csv')
        parser.add_argument('--tarefas', type=str, required=True, help='Caminho do arquivo tarefa.csv')

    def handle(self, *args, **kwargs):
        projetos_csv = kwargs['projetos']
        tarefas_csv = kwargs['tarefas']

        self.stdout.write(self.style.WARNING("Iniciando importação..."))

        self.stdout.write(self.style.WARNING("Importando Projetos..."))

        with open(projetos_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Projeto.objects.get_or_create(
                    nome=row['nome'],
                    defaults={
                        'descricao': row['descricao'],
                        'data_criacao': row['data_criacao']
                    }
                )

        self.stdout.write(self.style.SUCCESS("Projetos importados com sucesso!"))

        self.stdout.write(self.style.WARNING("Importando Tarefas..."))

        with open(tarefas_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                projeto_id = int(row['projeto'])
                try:
                    projeto = Projeto.objects.get(id=projeto_id)
                except Projeto.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Projeto com ID {projeto_id} não encontrado. Pulando..."))
                    continue

                Tarefa.objects.get_or_create(
                    titulo=row['titulo'],
                    projeto=projeto,
                    defaults={
                        'status': row['status'],
                        'prioridade': row['prioridade'],
                        'data_limite': row['data_limite']
                    }
                )

        self.stdout.write(self.style.SUCCESS("Tarefas importadas com sucesso!"))
        self.stdout.write(self.style.SUCCESS("Importação finalizada!"))