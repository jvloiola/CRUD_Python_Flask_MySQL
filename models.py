from main import insert, select, update, delete


"""_________________CRUD DIRETORES________"""
def inserir_diretores (nome_completo):
    insert("diretores", ["nome_completo"],[nome_completo])

def alterar_diretores (id):
    update("diretores","id",id,"nome_completo")

def apagar_diretores (id):
    delete ("diretores","id",id)

def buscar_diretores (id):
    select("diretores","id",id)

"""________________CRUD GENEROS_________"""
def inserir_generos (id):
    insert("generos", ["nome"],[nome])

def alterar_generos (id):
    update("generos","id",id,"nome")

def apagar_generos (id):
    delete ("generos","id",id)

def buscar_generos (id):
    select("generos","id",id)

"""______________CRUD FILMES____________"""
def inserir_filmes (id):
    insert("filmes","colunas","valores")

def alterar_filmes (id):
    update("filmes","id",id,"nome")

def apagar_filmes (id):
    delete ("filmes","id",id)

def buscar_filmes ():
    select("filmes","id",id)

"""______________CRUD USUARIO___________"""
def inserir_usuario (nome_completo):
    insert("usuario","colunas","valores")

def alterar_usuario (id):
    update("usuario","id",id,"nome")

def apagar_usuario (id):
    delete ("usuario","id",id)

def buscar_usuario ():
    select("usuario","id",id)
