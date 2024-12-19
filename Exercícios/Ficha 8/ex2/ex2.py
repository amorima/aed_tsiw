'''
Este pequeno jogo deve basear-se no ficheiro paises.txt  (que contém uma 
lista de países). O seu jogo consiste em tentar adivinhar o nome do país, funcionando 
da seguinte forma: 
• Deve ler o ficheiro paises.txt para uma lista e em seguida sortear, aleatoriamente, 
um país da lista, em função da dimensão da própria lista.  
• Deve dispor no máximo de 3 tentativas para o utilizador acertar no nome do país.  
• Antes de cada tentativa, deve invocar a função imprimePais(), que funciona como 
uma ajuda ao utilizador: a função deve imprimir tantos “-“  quantos os caracteres 
que constituem o nome do país sorteado. A cada tentativa, a função deve desven-
dar um novo caracter do nome do país, como surge nas imagens abaixo.
'''

import os
import random

def ficheiro_existe():
    """Verifica se o ficheiro existe no filepath, caso não exista cria-o
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="utf-8"):
            pass



def ler_texto():
    with open(file_path, "r", encoding="utf-8") as ficheiro:
        paises=ficheiro.readlines()
        pais_aleatorio=random.choice(paises)
        return pais_aleatorio

def imprime_pais(pais, contador):
    nome=list(pais)
    if contador == 1:
        print(f"\n\t\t{nome[0]}{(len(nome)-2)*" -"}")
    elif contador == 2:
        print(f"\n\t\t{nome[0]} {nome[1]}{(len(nome)-3)*" -"}")
    elif contador == 3:
        print(f"\n\t\t{nome[0]} {nome[1]} {nome[2]}{(len(nome)-4)*" -"}")





#---------INÍCIO DO PROGRAMA-----------------
#Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
#Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)
nome_ficheiro = "paises.txt"
#Constroi os path corretos para diferentes sistemas operativos.
file_path = os.path.join("ficheiros", nome_ficheiro)

pais=ler_texto()
contador=0

os.system("cls")
print("\t\tAdivinhe o nome do país\n")
for x in range(3):
    contador+=1
    imprime_pais(pais, contador)
    tentativa=input("\nQual é o país? ")
    if tentativa.strip() == pais.strip():
        print("\nACERTOU!!!")
        exit()

print("\nNÃO ACERTOU")