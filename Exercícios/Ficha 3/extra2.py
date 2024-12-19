'''
Escreva a função countWord que receba um texto e uma palavra de pesquisa. A função deve de-
volver o número de ocorrências dessa palavra no texto, e as posições onde ocorre. 
 
Exemplo: 
Texto: Através de uma unidade de GPS/GPRS instalada em cada veículo um aparelho de monitoriza-
ção regista informação em tempo real sobre a localização de cada veículo  
 
countWord(texto, ‘veículo’)    =>    devolve 2   ( 2 ocorrências)
'''

import os

# Limpa a consola
os.system("cls")

def count_word(texto,pesquisa):
    contador=0
    posicoes=""
    contador_posicao=0
    texto.replace("."," ")
    texto.replace(","," ")
    texto=texto.lower()
    texto_pesquisa=texto.split()
    for i in texto_pesquisa:
        contador_posicao+=1
        if i == pesquisa.lower():
            contador+=1
            posicoes+=f"{contador_posicao} "
    return contador, posicoes


# Solicita o input do utilizador
texto = input("Indique um texto: ")
pesquisa = input("\nPesquisa: ")
repeticoes,posicoes=count_word(texto,pesquisa)
print(f"\nA palavra {pesquisa} ocorre {repeticoes} vezes no texto, nas posições {posicoes}\n")