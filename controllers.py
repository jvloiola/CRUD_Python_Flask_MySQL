from flask import Flask, jsonify, request
from main import *
from decimal import Decimal
from models import *
from serializadores import *
from validacao import *


app = Flask(__name__)

#-------------------------CRUD USUARIO-------------------------
@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return None, 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})

@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


#-------------------------CRUD FILME-------------------------
@app.route("/filme", methods=["POST"])
def inserir_filme():
    filme = filme_from_web(**request.json)  
    if valida_filme(**usuario):
        id_filme = insert_filme(**usuario)
        filme_cadastrado = get_filme(id_usuario)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "filme inválido"})

@app.route("/filme/<int:id>", methods=["PUT", "PATCH"])
def alterar_filme(id):
    filme = filme_from_web(**request.json)  
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_from_db(filme_cadastrado))
    else:
        return jsonify({"erro": "filme inválido"})

@app.route("/filme/<int:id>", methods=["DELETE"])
def apagar_filme(id):
    try:
        delete_filme(id)
        return None, 204
    except:
        return jsonify({"erro": "filme possui itens conectados a ele"})

@app.route("/filme", methods=["GET"])
def buscar_filme():
    nome_completotitulo = titulo_from_web(**request.args)
    filme = select_filme(nome_completo)
    filme_from_db = [filme_from_db(filme) for filme in filme]
    return jsonify(filme_from_db)

    #--------------------CRUD GENERO--------------------------------
@app.route("/genero", methods=["POST"])
def inserir_genero():
    genero = genero_from_web(**request.json)  
    if valida_genero(**usuario):
        id_genero = insert_genero(**usuario)
        genero_cadastrado = get_genero(id_usuario)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "genero inválido"})

@app.route("/genero/<int:id>", methods=["PUT", "PATCH"])
def alterar_genero(id):
    genero = genero_from_web(**request.json)  
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_from_db(genero_cadastrado))
    else:
        return jsonify({"erro": "genero inválido"})

@app.route("/genero/<int:id>", methods=["DELETE"])
def apagar_genero(id):
    try:
        delete_genero(id)
        return None, 204
    except:
        return jsonify({"erro": "genero possui itens conectados a ele"})

@app.route("/genero", methods=["GET"])
def buscar_genero():
    nome_completo = genero_from_web(**request.args)
    genero = select_genero(nome_completo)
    genero_from_db = [genero_from_db(genero) for genero in genero]
    return jsonify(genero_from_db)


#-------------------------CRUD DIRETOR-------------------------
@app.route("/diretor", methods=["POST"])
def inserir_diretor():
    diretor = diretor_from_web(**request.json)  
    if valida_diretor(**usuario):
        id_diretor = insert_diretor(**usuario)
        diretor_cadastrado = get_diretor(id_usuario)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "diretor inválido"})

@app.route("/diretor/<int:id>", methods=["PUT", "PATCH"])
def alterar_diretor(id):
    diretor = diretor_from_web(**request.json)  
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_from_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "diretor inválido"})

@app.route("/diretor/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    try:
        delete_diretor(id)
        return None, 204
    except:
        return jsonify({"erro": "diretor possui itens conectados a ele"})

@app.route("/diretor", methods=["GET"])
def buscar_diretor():
    nome_completo = nome_diretor_from_web(**request.args)
    diretor = select_diretor(nome_completo)
    diretor_from_db = [diretor_from_db(usuadiretorrio) for diretor in diretor]
    return jsonify(diretor_from_db)



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

