# ---------------------DIRETORES----------------------------------
def diretor_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
    }


def diretor_from_db(*args):
    return {
        "nome_completo": args[0]
    }


# --------------------GENEROS------------------------------------
def genero_from_web(**kwargs):
    return {
        "nome": kwargs["nome"] if kwargs["nome"] else "",
    }


def genero_from_db(*args):
    return {
        "nome": args[0]
    }


# --------------------FILMES------------------------------------
def filme_from_web(**kwargs):
    return {
        "titulo": kwargs["titulo"] if kwargs["titulo"] else "",
        "ano": kwargs["ano"] if kwargs["ano"] else "",
        "classificacao": kwargs["classificacao"] if kwargs["classificacao"] else "",
        "preco": kwargs["preco"] if kwargs["preco"] else ""
    }


def filme_from_db(*args):
    return {
        "nome": args[0]
    }


# ----------------------USUARIO---------------------------------
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if kwargs["titulo"] else "",
        "CPF": kwargs["cpf"] if kwargs["cpf"] else ""
    }


def usuario_from_db(*args):
    return {
        "nome-completo": args[0]
    }
