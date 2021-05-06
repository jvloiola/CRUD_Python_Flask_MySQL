from models import *

"""Aqui são feitas as validações dos dados vindos da web."""

def valida_diretor(nome_completo,**kwargs):
    if len(nome_completo) == "":
        return False

def valida_genero(id,):
    if len(id) == 0:
        return False

def valida_filme(id):
    if id == 0:
        return False