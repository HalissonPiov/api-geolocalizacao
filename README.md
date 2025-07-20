# 🌍 GeoAPI - API de Geolocalização com FastAPI

Este projeto é uma API REST para gerenciamento de usuários e pontos geográficos de interesse, desenvolvida com o framework **FastAPI** e banco de dados **SQLite**. A API oferece endpoints para criar, listar, atualizar e remover usuários e pontos, com foco em organização, boas práticas e testes automatizados.

---

## 📌 Contexto da Aplicação

A ideia surgiu da necessidade de uma aplicação backend simples e eficiente para registrar **pontos geográficos** relacionados a usuários. Esse tipo de sistema pode ser utilizado em:

- Aplicativos de turismo, para marcar locais visitados;
- Plataformas de mobilidade urbana;
- Sistemas de gerenciamento de entregas ou coleta de dados em campo.

O foco foi desenvolver uma **API limpa, rápida e testável**, que sirva de base para futuros projetos com frontend, como aplicativos móveis ou web.

---

## 🚀 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| [**FastAPI**](https://fastapi.tiangolo.com/) | Criação rápida de APIs REST com suporte a validação automática e documentação Swagger/OpenAPI |
| [**SQLite**](https://www.sqlite.org/index.html) | Banco de dados leve e embutido para armazenamento local |
| [**SQLModel**](https://sqlmodel.tiangolo.com/) | ORM moderno baseado em Pydantic e SQLAlchemy |
| [**Pytest**](https://docs.pytest.org/) | Framework de testes em Python |
| [**UUID**](https://docs.python.org/3/library/uuid.html) | Identificação única de usuários e pontos |

---

## ️✅ Funcionalidades da API 
### 🙍🏻 Usuários
- **POST /AdicionarUsuario/**
- **PUT /AtualizarUsuario/**
- **GET /ListarUsuario/**
- **DELETE /RemoverUsuario/**

### 🚩 Pontos Geográficos
- **POST /AdicionarPonto/**
- **PUT /AtualizarPonto/**
- **GET /ListarPontosPorUsuario/**
- **DELETE /RemoverPonto/**

---

## ➡️ Como Executar

### 💻 Aplicação:

1. Instale as dependências

    <code> pip install -r requirements.txt </code>


2. Rode o servidor

    <code> uvicorn app.main:app --reload </code>


3. Acesse a documentação automática via Swagger para interagir com a API

    http://localhost:8000/docs

### 🧪 Testes:

1.  Execute o comando

    <code> pytest </code>

- Se necessário, em caso de erro, tente executar primeiro

    <code> $env:PYTHONPATH="." </code>