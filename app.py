from flask import Flask, jsonify, request
from main import query, execute
from decimal import Decimal


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return jsonify(query("SHOW schemas"))
    elif request.method == "POST":
        return request.json

@app.route("/usuarios", methods=["POST"])
def login():
    email = request.json["email"]
    senha = request.json["senha"]
    return jsonify(query(f"SELECT * FROM usuarios WHERE email = %s and senha=%s", (email, senha)))

def update(tabela, chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {chave} = %s""", valores + [valor_chave])

def insert(tabela, colunas, valores):
    execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for valor in valores])})", valores)

qery("SELECT * FROM idiomas WHERE id = %s",(id,)))


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
