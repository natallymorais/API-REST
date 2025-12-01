# API-REST 🛠️  
Sistema de gestão de **Projetos** e **Tarefas** — backend em Django + Django REST Framework  

## 🔎 Visão Geral  
Essa API permite criar, listar, atualizar e deletar **Projetos** e suas **Tarefas** associadas (relação 1:N). Também permite filtrar tarefas por projeto. Suporta autenticação via token e está documentada com OpenAPI/Swagger.

---

## ✅ Funcionalidades  

- CRUD completo de **Projeto**  
- CRUD completo de **Tarefa**  
- Filtro de tarefas por projeto (`/api/tarefas/?projeto=<id>`)  
- Autenticação via token (`/api-token-auth/`)  
- Documentação interativa da API (Swagger / Redoc)  

---

## 📦 Tecnologias utilizadas  

- Python  
- Django  
- Django REST Framework  
- Django REST Framework Authtoken  
- drf-spectacular (OpenAPI / Swagger)  

---

## 🚀 Como rodar localmente  
 bash  
# 1. Clone o repositório  
git clone https://github.com/natallymorais/API-REST.git  
cd API-REST  

# 2. Crie e ative um ambiente virtual  
python -m venv venv  
# Windows  
venv\Scripts\activate  
# Linux / macOS  
source venv/bin/activate  

# 3. Instale as dependências  
pip install -r requirements.txt  # se você tiver esse arquivo  
# ou manualmente:
pip install django djangorestframework djangorestframework-authtoken drf-spectacular  

# 4. Aplique as migrações  
python manage.py migrate  

# 5. Crie um superusuário (opcional, para acessar o admin e gerar token)  
python manage.py createsuperuser  

# 6. Rode o servidor de desenvolvimento  
python manage.py runserver  

A API estará disponível em: http://127.0.0.1:8000/  

📚 Endpoints principais  
Caminho	Método	Descrição  
/api/projetos/	GET	Lista projetos  
/api/projetos/	POST	Cria novo projeto  
/api/projetos/{id}/	GET	Detalha projeto  
/api/projetos/{id}/	PUT/PATCH	Atualiza projeto  
/api/projetos/{id}/	DELETE	Deleta projeto  
/api/tarefas/	GET	Lista tarefas  
/api/tarefas/?projeto=<id>	GET	Lista tarefas de um projeto  
/api/tarefas/	POST	Cria nova tarefa  
/api/tarefas/{id}/	GET	Detalha tarefa  
/api/tarefas/{id}/	PUT/PATCH	Atualiza tarefa  
/api/tarefas/{id}/	DELETE	Deleta tarefa  
/api-token-auth/	POST	Autenticação (obter token)  

🔐 Autenticação  

Para rotas protegidas (POST/PUT/PATCH/DELETE), use:

Authorization: Token <seu_token>

📄 Documentação da API

Você pode acessar a documentação interativa da API em:

Swagger UI: http://localhost:8000/api/docs/

Redoc: http://localhost:8000/api/redoc/

🧪 Testando a API

Você pode usar ferramentas como:

Postman

Insomnia

Thunder Client (VS Code)

Qualquer cliente HTTP

Siga o fluxo:

Obter token via /api-token-auth/

Incluir o header Authorization: Token <seu_token> nas requisições protegidas

Executar CRUD de Projetos e Tarefas

Fazer requisição GET para /api/tarefas/?projeto=<i­d_do_projeto> para filtrar

✨ Possíveis melhorias

Validações adicionais (ex: verificar data_limite)

Paginação nas listagens

Endpoints para marcação em lote de tarefas (ex: concluir várias de uma vez)

Sistema de usuários e permissões mais elaboradas

🧑‍💻 Contribuindo

Fork o repositório

Crie uma branch com a feature (feature/nova-funcionalidade)

Commit suas alterações (git commit -m 'feat: descrição')

Push para sua branch

Envie um pull request

