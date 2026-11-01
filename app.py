import os
import sqlite3

import yaml
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

# Pasta onde está o app.py (para achar o config.yml de qualquer lugar)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def carregar_config():
    # Lê o config.yml e devolve como dicionário
    caminho = os.path.join(BASE_DIR, "config.yml")
    with open(caminho, encoding="utf-8") as f:
        return yaml.safe_load(f)


config = carregar_config()

app = Flask(__name__)
# Chave usada para proteger a sessão (login) no próximo passo
app.secret_key = config["app"]["secret_key"]


def conectar():
    # Nome do banco vem do config.yml
    return sqlite3.connect(config["database"]["arquivo"])


def criar_tabela():
    con = conectar()
    con.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            senha_hash TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()


criar_tabela()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    # Próximo passo: conferir no banco com check_password_hash
    return "Dados recebidos"


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        senha_hash = generate_password_hash(senha)
        try:
            con = conectar()
            # Os ? protegem contra injeção de SQL
            con.execute(
                "INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)",
                (usuario, senha_hash)
            )
            con.commit()
            con.close()
            return "Usuário cadastrado!"
        except sqlite3.IntegrityError:
            return "Esse usuário já existe."
    return render_template("cadastro.html")


if __name__ == "__main__":
    # debug vem do config.yml (deixe false fora dos estudos)
    app.run(debug=config["app"]["debug"])