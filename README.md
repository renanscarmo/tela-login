# Tela Login — Flask

Projeto de estudo em Python/Flask: tela de login com tema Matrix, cadastro de usuários com senha em hash e análise de segurança automatizada a cada push.

## Funcionalidades

- Tela de login em HTML, CSS e JavaScript (tema Matrix preto e verde)
- Cadastro de usuários com senha protegida por hash (Werkzeug)
- Banco de dados SQLite com usuários únicos
- Consultas com parâmetros (`?`) para evitar injeção de SQL
- Configurações em `config.yml`, fora do código
- Pipeline de segurança no GitHub Actions: SAST (Bandit) e SCA (pip-audit)

## Tecnologias

Python 3.12+ · Flask · SQLite · PyYAML · HTML/CSS/JS · GitHub Actions

## Estrutura

```
Tela-Login/
├── app.py                 # aplicação Flask (rotas e banco)
├── config.example.yml     # modelo de configuração
├── requirements.txt       # dependências
├── templates/             # index.html, cadastro.html
├── static/                # style.css, script.js
└── .github/workflows/     # seguranca.yml (Bandit + pip-audit)
```

## Como executar

```bash
git clone https://github.com/renanscarmo/tela-login.git
cd tela-login
pip install -r requirements.txt
cp config.example.yml config.yml   # Windows: copy config.example.yml config.yml
```

Edite o `config.yml` e troque `secret_key` por uma chave própria:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Rode o servidor:

```bash
python app.py
```

Acesse `http://127.0.0.1:5000` (login) e `http://127.0.0.1:5000/cadastro` (cadastro).

## Segurança

- Senhas nunca são guardadas em texto puro, apenas o hash
- `config.yml` e `usuario.db` ficam fora do repositório (`.gitignore`)
- A cada push, o GitHub Actions roda o **Bandit** (análise do código) e o **pip-audit** (vulnerabilidades nas dependências)
- `debug=True` é só para estudo e não deve ser usado em produção

## Próximos passos

- [ ] Login com verificação da senha (`check_password_hash`)
- [ ] Sessão de usuário com tempo limite
- [ ] Perfis de usuário (comum e administrador)
- [ ] Bloqueio após tentativas erradas
- [ ] Registro de acessos (log)

## Autor

renanscarmo — estudante de tecnologia, com foco em Python e segurança.

