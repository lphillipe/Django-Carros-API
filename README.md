# 🚗 Django Carros API

API e sistema web para gerenciamento de carros, desenvolvido com Django. O projeto contempla autenticação de usuários, CRUD completo de veículos e integração com IA para enriquecimento de dados.

---

## 📌 Visão Geral

Este projeto foi desenvolvido com foco em backend utilizando Django, aplicando boas práticas de organização, separação de responsabilidades e estrutura modular.

A aplicação permite:

- Cadastro e autenticação de usuários
- Gerenciamento de carros (CRUD)
- Upload de imagens dos veículos
- Organização por marcas
- Controle de inventário
- Integração com IA para geração de descrições

---

## 🧱 Arquitetura do Projeto

```
Django-Carros-API/
│
├── accounts/        # Autenticação e usuários
├── cars/            # Regras de negócio (carros)
├── app/             # Configuração principal do Django
├── groq_ai/         # Integração com IA
├── templates/       # Templates HTML
└── manage.py
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Django
- SQLite (default)
- HTML/CSS (templates)
- Poetry
- Integração com API de IA

---

## 🚀 Como Rodar o Projeto

```bash
git clone https://github.com/lphillipe/Django-Carros-API.git
cd Django-Carros-API
poetry install
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Acesse http://127.0.0.1:8000/cars/ para visualizar a aplicação.
```

---

## 📊 Funcionalidades

- Autenticação de usuários
- CRUD de carros
- Upload de imagens
- Controle de estoque
- Geração de descrições com IA

---

## 🧪 Testes

```bash
python manage.py test
```

---

## 📦 Roadmap

- API REST (DRF)
- JWT
- Docker
- CI/CD
- Deploy com Kubernetes

---

## 📄 Licença

Projeto para portfólio.

---

## 👨‍💻 Autor

Phillipe