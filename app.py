from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Caminho do banco de dados
CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), "tarefas.db")


# Conectar ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


# Criar a tabela de tarefas
def criar_tabela():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            concluida INTEGER NOT NULL DEFAULT 0,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()


# Página inicial: listar tarefas
@app.route("/")
def index():
    conexao = conectar_banco()

    tarefas = conexao.execute("""
        SELECT * FROM tarefas
        ORDER BY id DESC
    """).fetchall()

    conexao.close()

    return render_template("index.html", tarefas=tarefas)


# Adicionar uma nova tarefa
@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form.get("titulo", "").strip()

    if titulo:
        conexao = conectar_banco()

        conexao.execute(
            "INSERT INTO tarefas (titulo) VALUES (?)",
            (titulo,)
        )

        conexao.commit()
        conexao.close()

    return redirect(url_for("index"))


# Atualizar o status da tarefa
@app.route("/concluir/<int:id>", methods=["POST"])
def concluir(id):
    conexao = conectar_banco()

    conexao.execute("""
        UPDATE tarefas
        SET concluida = CASE
            WHEN concluida = 0 THEN 1
            ELSE 0
        END
        WHERE id = ?
    """, (id,))

    conexao.commit()
    conexao.close()

    return redirect(url_for("index"))


# Excluir uma tarefa
@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    conexao = conectar_banco()

    conexao.execute(
        "DELETE FROM tarefas WHERE id = ?",
        (id,)
    )

    conexao.commit()
    conexao.close()

    return redirect(url_for("index"))


# Iniciar o sistema
if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)