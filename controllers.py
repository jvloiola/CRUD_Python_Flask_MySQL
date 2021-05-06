from flask import Flask, jsonify, request
from main import query, execute
from models import *
from serializadores import diretor_from_web, diretor_from_db
from validacao import *
from serializadores import *

app = Flask (__name__)

#-------------------------------INSERIR--------------------------------------
@app.route ("/diretores", methods = ["POST"])  # 1 - Checa a rota
def inserir_diretores ():
    diretor = diretor_from_web (**request.json)  # 3 - formata o que vem da internet
    if valida_diretor (**diretor):  # 2 - checa se os valores que vieram da internet são validos
        inserir_diretores (**diretor)  # 4- manda inserir o estado no banco de dados
        diretor_criado = buscar_diretores ([diretor ("id")])  # 5- puxa estado criado do banco de dados
        return jsonify (diretor_from_db (diretor_criado))  # 6 - retorna estado formatado pro usuário
    else:
        return jsonify ({"erro": "diretor inválido"})


@app.route ("/generos", methods = ["POST"])
def inserir_generos ():
    if valida_genero (id):
        genero = genero_from_web (**request.json)
        inserir_generos (**genero)
        genero_criado = buscar_generos ([genero ("id")])
        return jsonify (genero_from_db (genero_criado))
    else:
        return jsonify ({"erro": "genero invalido"})


@app.route ("/filmes", methods = ["POST"])
def inserir_filmes ():
    if valida_filme (id):
        genero = filme_from_web (**request.json)
        inserir_filmes (**genero)
        filme_criado = buscar_filme ([genero ("id")])
        return jsonify (filme_from_db (filme_criado))
    else:
        return jsonify ({"erro": "filme invalido"})









#----------------------------ALTERAR----------------------------------
@app.route ("/diretores/<int:id>", methods = ["PUT"])
def alterar_diretores (id):


@app.route ("/diretores/<int:id>", methods = ["DELETE"])
def apagar_diretores (id):


@app.route ("/diretores/<int:id>", methods = ["GET"])
def listar_diretores ():


def cria_estado ():
    # movido pra estado_from_web
    sigla = request.json ["sigla"]
    nome = request.json ["nome"]

    # movido pra insert_estado
    insert ("estados", ["sigla", "nome"], [sigla, nome])

    # movi para get_estado
    estado = select ("estados", "sigla", sigla)

    # melhorei usando estado_from_db
    return jsonify (estado)


@app.route ("/estados/<int:id>", methods = ["PUT"])
def alterar_estado (id):
    pass


@app.route ("/estados/<int:id>", methods = ["DELETE"])
def apagar_estado (id):
    pass


@app.route ("/estados", methods = ["GET"])
def listar_estados ():
    pass
