### Impulso Digital

O projeto **Impulso Digital** é uma aplicação web desenvolvida em Django para gerenciamento de funcionários e processos internos.

## Tecnologias Utilizadas
* [Python 3.x] (https://www.python.org/)
* [Django] (https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/index.html) (Banco de dados padrão)
* Bootstrap

## Como rodar o projeto localmente

Siga os passos abaixo para configurar o ambiente de desenvolvimento em sua máquina:

### 1. Clonar o repositório
```bash
git clone [https://github.com/joaovictorSsouza/impulso_digital.git](https://github.com/joaovictorSsouza/impulso_digital.git)
cd impulso_digital
```
### 2. Criar e ativar o Ambiente Virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```
### 4. Rodar as migrações do banco de dados
```bash
python manage.py migrate
```
### 5. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

### Estrutura do Projeto

```text
impulso_digital/
├── app/                  # Configurações centrais do Django (settings, urls, wsgi)
├── employee/             # App principal (Modelos de funcionários, Views, etc)
│   ├── migrations/       # Histórico de alterações do banco de dados
│   ├── templates/        # Arquivos HTML específicos do app employee
│   └── ...
├── templates/            # Templates globais (como o base.html)
├── .gitignore            # Arquivos ignorados pelo Git
├── db.sqlite3            # Banco de dados local (não enviado ao Git)
├── manage.py             # Utilitário de linha de comando do Django
└── requirements.txt      # Lista de dependências do projeto
```

---
## 👤 Autor

Desenvolvido por **João Victor Souza** Entre em contato:

[![LinkedIn]([www.linkedin.com/in/joão-victor-azevedo-de-souza-000a9834b](https://www.linkedin.com/in/joão-victor-azevedo-de-souza-000a9834b/))









