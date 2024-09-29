import os
from extensoes import extensoes_arquivo
from funcoes import *


def identifica_arquivo(path_pasta):
    # passa por cada arquivo para verificar se ele é um arquivo
    for arquivo in os.listdir(path_pasta):
        if os.path.isfile(arquivo):
            # se a variavel arquivo é diferente de pasta ela é um arquivo
            nome_pasta = "outros"
            for extensao, nome in extensoes_arquivo.items():
                if extensao in arquivo:
                    nome_pasta = nome
            mover_para_pasta(arquivo, nome_pasta, path_pasta)

def mover_para_pasta(arquivo, nome_pasta, path_pasta):
    novo_path = f"{path_pasta}/{nome_pasta}"
    if not pasta_existe(nome_pasta, path_pasta):
        cria_pasta(nome_pasta)
    else:
        # Verifica se arquivo existe na pasta
        if arquivo in os.listdir(novo_path):
            print(f"'{arquivo}' Arquivo já existe em {nome_pasta}")
            return
    mudar_diretorio_para(path_pasta)
    move_arquivo(arquivo, novo_path)
    informar(arquivo, novo_path)
            
def organiza_pasta(entrada):
    path_pasta = entrada.get()
    mudar_diretorio_para(path_pasta)
    identifica_arquivo(path_pasta)
