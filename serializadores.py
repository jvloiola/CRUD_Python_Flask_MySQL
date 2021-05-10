

#--------------------#SERIALIZADORES USUARIO#--------------------#
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }

def usuario_from_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"]
    }

def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""

#--------------------#SERIALIZADORES FILME#--------------------#
def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
    }

def filme_from_db(filme):
    return {
        "titulo": usuario["titulo"],
        "ano": usuario["ano"],
        "classificacao": usuario["classificacao"],
        "preco": preco["preco"]
    }

def titulo_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""


#--------------------#SERIALIZADORES GENERO#--------------------#
def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if "nome" in kwargs else "",
        "id": kwargs["id"] if "id" in kwargs else "",
    }

def genero_from_db(genero):
    return {
        "id": genro["id"],
        "nome": genero["nome_completo"]
        
    }

def genero_from_web(**kwargs):
    return kwargs["genero"] if "genero" in kwargs else ""


#--------------------#SERIALIZADORES GENERO#--------------------#
def diretores_from_web(**kwargs):
    return{
        "id": kwargs["id"] if "id" in kwargs else "",
        "nome_completo":kwargs["nome_completo"] if "nome_completo" in kwargs else
    }

def diretores_from_db(diretores):
    return {
        "id":diretores["id"],
        "nome_completo";diretores["nome_completo"]
    }
