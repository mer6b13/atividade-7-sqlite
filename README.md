# Atividade 7 — Banco de Dados com SQLite

## Descrição

Projeto desenvolvido com Python, Flask e SQLite para gerenciamento de tarefas, permitindo cadastrar, visualizar, concluir e excluir tarefas.

## Tecnologias utilizadas

- Python
- Flask
- SQLite
- HTML
- CSS

## Funcionalidades

- Cadastro de tarefas.
- Listagem de tarefas.
- Atualização do status das tarefas.
- Exclusão de tarefas.
- Registro da data de criação.
- Persistência dos dados utilizando SQLite.

## Estrutura do projeto

```text
atividade-7/
├── app.py
├── tarefas.db
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

## Como executar

1. Clone o repositório.
2. Entre na pasta do projeto.
3. Crie um ambiente virtual:

```bash
python3 -m venv venv
```

4. Ative o ambiente virtual:

```bash
source venv/bin/activate
```

5. Instale o Flask:

```bash
pip install flask
```

6. Execute a aplicação:

```bash
python app.py
```

7. Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Banco de dados

O projeto utiliza SQLite para armazenar as tarefas permanentemente.

A tabela `tarefas` possui os seguintes campos:

- `id`: identificador da tarefa.
- `titulo`: descrição da tarefa.
- `concluida`: status da tarefa.
- `data_criacao`: data de criação.

## Objetivo

Praticar persistência de dados, operações SQL básicas e integração entre Python, Flask e SQLite.