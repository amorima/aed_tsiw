'''' Escreva a função escreveTexto(texto) que receba um texto (lido, p.e. através de um in-
put) e o guarde num ficheiro binário, com a designação de dados.bin. Se o ficheiro não 
existir, deve ser criado com a path .\\ficheiros\\dados.bin. '''

import os

def ficheiro_existe():
    """Verifica se o ficheiro existe no filepath, caso não exista cria-o
    """
    if not os.path.exists(file_path):
        with open(file_path, 'wb'):
            pass

def escreve_texto(texto):
    """Recebe um texto, converte para binário e depois escreve no ficheiro

    Args:
        texto (str): texto input
    """
    ficheiro_existe()
    texto_bin=bytes(texto, encoding="utf-32")
    with open(file_path, 'wb') as ficheiro:
        ficheiro.write(texto_bin)

#-----------------------------------
#Início do programa

nome_ficheiro = "dados.bin"
#Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
#Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)
nome_ficheiro = "paises.txt"
#Constroi os path corretos para diferentes sistemas operativos.
file_path = os.path.join("ficheiros", nome_ficheiro)
texto=input("Escreva um pequeno texto: ")
escreve_texto(texto)




