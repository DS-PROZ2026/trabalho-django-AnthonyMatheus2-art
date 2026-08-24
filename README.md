# Projeto Django — Controle de Equipamentos

Aplicação Django para cadastrar, consultar, editar e excluir equipamentos.

## GitHub Codespaces

1. Abra este repositório no GitHub.
2. Crie um novo Codespace a partir da branch principal.
3. O `.devcontainer` instala as dependências e executa as migrações.
4. A aplicação inicia na porta `8000`.

Se precisar executar manualmente:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

O projeto usa SQLite por padrão. O arquivo `db.sqlite3` é criado automaticamente pelas migrações.

## Testes

```bash
python manage.py test
```

## Variáveis de ambiente

O Codespace cria `.env` a partir de `.env.example`. O `.env` não deve ser versionado.
