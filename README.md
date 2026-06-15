# Plataforma Educa+

Repositório de materiais didáticos desenvolvido para a disciplina de Fundamentos de Bancos de Dados — UFC 2026.1.

---

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [PostgreSQL 14+](https://www.postgresql.org/download/)
- pip

---

## Configuração do banco de dados

### 1. Abra o psql (ou pgAdmin) e crie o schema

```sql
CREATE SCHEMA IF NOT EXISTS fdb;
```

### 2. Crie as tabelas

No terminal, dentro da pasta do projeto:

```bash
psql -U postgres -c "SET search_path TO fdb;" -f create.sql
```

### 3. Popule com dados de exemplo

```bash
psql -U postgres -c "SET search_path TO fdb;" -f insert.sql
```

> Se o psql pedir senha, adicione `PGPASSWORD=sua_senha` antes do comando:
> ```bash
> PGPASSWORD=sua_senha psql -U postgres -c "SET search_path TO fdb;" -f create.sql
> ```
> No Windows (PowerShell):
> ```powershell
> $env:PGPASSWORD = "sua_senha"; psql -U postgres -c "SET search_path TO fdb;" -f create.sql
> $env:PGPASSWORD = "sua_senha"; psql -U postgres -c "SET search_path TO fdb;" -f insert.sql
> ```

---

## Instalação das dependências Python

```bash
pip install Flask Flask-SQLAlchemy psycopg2-binary typing_extensions
```

---

## Configuração da senha do banco

O projeto lê a senha do banco via variável de ambiente. **Cada pessoa define a sua própria senha localmente**, sem precisar alterar o código.

### Windows (PowerShell)

```powershell
$env:DB_PASS = "sua_senha"
python app.py
```

### Linux / Mac

```bash
DB_PASS=sua_senha python app.py
```

### Alternativa: editar direto no app.py

Se preferir, abra o `app.py` e troque o valor padrão:

```python
DB_PASS = os.getenv("DB_PASS", "sua_senha_aqui")
```

---

## Rodando o projeto

```bash
python app.py
```

Acesse em: **http://127.0.0.1:5000**

---

## Estrutura do projeto

```
fdb-projeto/
├── app.py              # Entry point
├── database.py         # Configuração do SQLAlchemy
├── models.py           # Modelos ORM (19 tabelas)
├── create.sql          # Script de criação do banco
├── insert.sql          # Script de inserção de dados
├── routes/             # Blueprints Flask
│   ├── menu.py         # Dashboard
│   ├── usuarios.py     # CRUD de usuários
│   ├── materiais.py    # CRUD de materiais
│   ├── avaliacoes.py   # CRUD de avaliações
│   ├── favoritos.py    # CRUD de favoritos
│   ├── historico.py    # Histórico de acessos
│   ├── colecoes.py     # CRUD de coleções
│   └── graficos.py     # Gráficos e analytics
└── templates/          # Templates HTML (Jinja2 + Tailwind)
```

---

## Divisão das telas por membro

| Membro | Telas | Gráfico |
|--------|-------|---------|
| Halyson | Usuários, Materiais | Votos de Utilidade |
| Kaua | Avaliações, Coleções | Notas dos Materiais |
| Marissa | Tags, Disciplinas, Comentários | — |
