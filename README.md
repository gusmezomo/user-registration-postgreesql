# PostgreSQL Learning

Projeto desenvolvido para aprender o funcionamento completo de uma aplicação utilizando PostgreSQL, FastAPI e JavaScript puro.

O objetivo é entender toda a comunicação entre:

Frontend → API → PostgreSQL.

---

# Tecnologias

- PostgreSQL
- FastAPI
- Python
- psycopg
- HTML
- CSS
- JavaScript
- DBeaver
- SQL

---

# Estrutura

backend/

- API FastAPI
- conexão com PostgreSQL
- rotas
- serviços
- validação

database/

- criação do banco
- inserts
- consultas SQL

frontend/

- interface HTML
- comunicação com a API

---

# Fluxo da aplicação

Frontend

↓

FastAPI

↓

Services

↓

PostgreSQL

---

# Funcionalidades

- Listar usuários
- Cadastrar usuários
- Documentação Swagger
- Validação utilizando Pydantic

---

# Como executar

## 1. Abrir o WSL

```bash
wsl
```

---

## 2. Iniciar o PostgreSQL

```bash
!startpost
```

ou

```bash
sudo systemctl start postgresql
```

---

## 3. Backend

```bash
cd backend

source .venv/bin/activate

uvicorn main:app --reload
```

API:

http://localhost:8000

Swagger:

http://localhost:8000/docs

---

## 4. Frontend

```bash
cd frontend

python3 -m http.server 5500
```

Abrir:

http://localhost:5500

---

# Estrutura do Banco

Tabela:

usuarios

Campos:

- id
- nome
- email
- senha
- ativo
- criado_em

---

# Próximas melhorias

- Editar usuário
- Excluir usuário
- Hash de senha
- Login
- JWT
- Docker

# Estrutura do Projeto

```text
postgresql-learning/
│
├── backend/
│   ├── .env
│   ├── requirements.txt
│   ├── database.py
│   ├── main.py
│   │
│   ├── routers/
│   │   └── usuarios.py
│   │
│   ├── schemas/
│   │   └── usuario.py
│   │
│   └── services/
│       └── usuario_service.py
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   ├── queries.sql
│   └── teste.sql
│
└── frontend/
    ├── index.html
    ├── script.js
    └── styles.css
```

---

# Organização do Backend

O backend foi organizado separando cada responsabilidade em um arquivo ou pasta específica. Essa abordagem facilita a manutenção do projeto e segue uma estrutura comum em aplicações desenvolvidas com FastAPI.

## `main.py`

É o ponto de entrada da aplicação.

Responsabilidades:

- Inicializar a aplicação FastAPI.
- Configurar o CORS.
- Registrar todas as rotas da aplicação.

Fluxo:

```
main.py

↓

FastAPI

↓

Routers
```

---

## `database.py`

Responsável apenas pela conexão com o PostgreSQL.

Não contém regras de negócio nem consultas SQL.

Responsabilidades:

- Ler as variáveis do arquivo `.env`.
- Criar uma conexão com o banco utilizando `psycopg`.
- Disponibilizar essa conexão para o restante da aplicação.

Fluxo:

```
Service

↓

database.py

↓

PostgreSQL
```

---

## `routers/`

Contém todas as rotas da API.

Cada arquivo representa um conjunto de endpoints relacionados.

Exemplo:

```
usuarios.py

↓

GET /usuarios

POST /usuarios
```

Responsabilidades:

- Receber as requisições HTTP.
- Validar os dados recebidos.
- Chamar os serviços responsáveis pela lógica da aplicação.
- Retornar a resposta ao cliente.

As rotas **não acessam diretamente o banco de dados**.

---

## `services/`

Contém a lógica de negócio da aplicação.

É nessa camada que ficam as operações realizadas no banco.

Responsabilidades:

- Buscar usuários.
- Inserir novos usuários.
- Atualizar registros.
- Excluir registros.

Os serviços utilizam `database.py` para obter uma conexão com o PostgreSQL.

Fluxo:

```
Router

↓

Service

↓

Database

↓

PostgreSQL
```

---

## `schemas/`

Contém os modelos utilizados pelo Pydantic.

São responsáveis pela validação dos dados recebidos e enviados pela API.

Exemplo:

`UsuarioCreate`

Define quais dados o cliente deve enviar para cadastrar um usuário.

```json
{
    "nome": "João",
    "email": "joao@email.com",
    "senha": "123456"
}
```

`UsuarioResponse`

Define quais dados serão retornados ao cliente.

```json
{
    "id": 1,
    "nome": "João",
    "email": "joao@email.com",
    "ativo": true,
    "criado_em": "2026-06-30T14:00:00"
}
```

Essa separação evita que informações sensíveis, como a senha, sejam retornadas pela API.

---

# Organização da pasta `database`

Essa pasta contém apenas arquivos SQL utilizados durante o desenvolvimento.

## `schema.sql`

Cria toda a estrutura do banco de dados.

Exemplo:

- criação de tabelas;
- constraints;
- chaves primárias;
- valores padrão.

É executado apenas uma vez para criar a estrutura inicial do banco.

---

## `seed.sql`

Insere dados de exemplo no banco.

Utilizado para facilitar testes durante o desenvolvimento.

---

## `queries.sql`

Arquivo utilizado para executar consultas SQL durante o desenvolvimento.

Exemplos:

- SELECT
- UPDATE
- DELETE
- JOIN

---

## `teste.sql`

Arquivo livre para testes temporários.

Utilizado para experimentar consultas sem alterar os demais scripts.

---

# Organização do Frontend

O frontend foi desenvolvido utilizando apenas HTML, CSS e JavaScript puro.

## `index.html`

Define toda a estrutura da página.

Responsável por:

- formulário;
- tabela;
- organização dos elementos.

---

## `styles.css`

Contém toda a estilização da aplicação.

Responsável por:

- layout;
- cores;
- espaçamentos;
- responsividade básica.

---

## `script.js`

Responsável pela comunicação entre o frontend e a API.

Funções principais:

- carregar usuários;
- cadastrar usuários;
- atualizar a tabela.

Fluxo:

```
Usuário

↓

JavaScript

↓

Fetch API

↓

FastAPI

↓

PostgreSQL

↓

JSON

↓

Tabela HTML

┌─────────────┐
│  Frontend   │
│ HTML/CSS/JS │
└──────┬──────┘
       │ HTTP (fetch)
       ▼
┌─────────────┐
│   FastAPI   │
│  (main.py)  │
└──────┬──────┘
       ▼
┌─────────────┐
│   Routers   │
└──────┬──────┘
       ▼
┌─────────────┐
│  Services   │
└──────┬──────┘
       ▼
┌─────────────┐
│ database.py │
└──────┬──────┘
       ▼
┌─────────────┐
│ PostgreSQL  │
└─────────────┘
```
