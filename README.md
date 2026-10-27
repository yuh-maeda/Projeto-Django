# Projeto Django — Hospital

Sistema web simples para cadastro de **pacientes**, **médicos** e **exames**, feito com Django usando class-based views.

## Funcionalidades

- Listagem, cadastro e exclusão de pacientes, médicos e exames
- Cada exame é vinculado a um médico responsável e a um paciente, com período (matutino, vespertino ou noturno)
- Paginação nas listas de pacientes e médicos (5 por página)
- Painel administrativo em `/admin/` com o tema [Jazzmin](https://github.com/farridav/django-jazzmin)
- Layout com [Bootstrap 6 (alpha)](https://getbootstrap.com/) via CDN e CSS próprio

## Tecnologias

- Python 3.13
- Django 6.1
- django-jazzmin 3.0
- SQLite (banco padrão do Django)

## Como rodar

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/yuh-maeda/Projeto-Django.git
   cd Projeto-Django
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install django django-jazzmin
   ```

4. Crie o banco de dados e um usuário administrador:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

   Acesse em http://127.0.0.1:8000/pacientes/.

## Rotas

| Rota | Descrição |
| --- | --- |
| `/pacientes/` | Lista de pacientes |
| `/pacientes/novo/` | Cadastro de paciente |
| `/pacientes/<id>/excluir/` | Exclusão de paciente |
| `/medicos/` | Lista de médicos |
| `/medicos/novo/` | Cadastro de médico |
| `/medicos/<id>/excluir/` | Exclusão de médico |
| `/exames/` | Lista de exames |
| `/exames/novo/` | Cadastro de exame |
| `/exames/<id>/excluir/` | Exclusão de exame |
| `/admin/` | Painel administrativo |

> Ao excluir um médico ou paciente, os exames vinculados a ele também são excluídos.

## Estrutura

```
Projeto-Django/
├── app/                    # Configurações do projeto (settings, urls)
├── hospital/               # App principal
│   ├── models.py           # Pacientes, Medicos e Exames
│   ├── forms.py            # ModelForms usados nos cadastros
│   ├── views.py            # ListView, CreateView e DeleteView
│   ├── urls.py             # Rotas do app (namespace "hospital")
│   ├── static/hospital/css/
│   └── templates/
│       ├── base.html       # Layout base
│       ├── partials/       # Navbar e footer
│       └── hospital/       # Templates de lista, cadastro e exclusão
└── manage.py
```