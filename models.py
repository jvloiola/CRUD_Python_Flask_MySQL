from main import *

#--------------------------#USUARIO#--------------------------#
def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id):
    return select("usuarios", "id", id)[0]

def update_usuario(id, nome_completo, CPF):
    update("usuarios", "id", id, ["nome_completo", "CPF"], [nome_completo, CPF])

def delete_usuario(id):
    delete("usuarios", "id", id)

def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)

#--------------------------#FILME#--------------------------#
def insert_filme(id):
    return insert("filmes", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], 
    [titulo, ano, classificacao, preco, diretores_id, generos_id])]

def get_filme(id):
    return select ("filmes","id", id)[0]

def update("filmes","id",["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
    [titulo, ano, classificacao, preco, diretores_id, generos_id])

def delete_filme(id):
    delete("filmes", "id", id)

def select_filmes(titulo):
    return select_like("filmes","titulo", titulo)

#--------------------------#GENERO#--------------------------#
def insert_genero(nome):
    return insert("genero", ["nome"], [nome])

def get_genero(id):
    return select("genero", "id", id)[0]

def update_genero(id, nome):
    update("genero", "id", id, ["nome"], [nome])

def delete_genero(id):
    delete("genero", "id", id)

def select_genero(nome):
    return select_like("genero", "nome", nome)

#--------------------------#DIRETORES#--------------------------#
def insert_diretores(nome_completo, id):
    return insert("usuarios", ["nome_completo", "id"], [nome_completo, id])

def get_diretores(id):
    return select("usuarios", "id", id)[0]

def update_diretores(id, nome_completo, id):
    update("usuarios", "id", id, ["nome_completo", "id"], [nome_completo, id])

def delete_diretores(id):
    delete("usuarios", "id", id)

def select_diretores(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)
