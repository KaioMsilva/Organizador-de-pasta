import shutil
import os

def move_arquivo(arquivo, nome_pasta):
    shutil.move(arquivo, nome_pasta)

def pasta_existe(nome_pasta, path_pasta):
    return nome_pasta in os.listdir(path_pasta)

def arquivo_existe(arquivo):
    return  os.path.isfile(arquivo)

def mudar_diretorio_para(path):
    os.chdir(path)

def mostrar_diretorio():
    print (os.getcwd())
    
def cria_pasta(nome_pasta):
    os.mkdir(nome_pasta)