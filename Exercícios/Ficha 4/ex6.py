'''Elabore um programa que leia uma lista de 10 números inteiros.  
Em seguida, dado um determinado valor de pesquisa, invoque a função searchNum-
ber(lista, pesquisa) que deve devolver as posições em que encontra o valor de pesquisa, 
na lista.  
Caso o valor de pesquisa não exista na lista, deve surgir uma mensagem adequada.'''

import os

# Limpa a consola
os.system("cls")

def search_number(numeros,pesquisa):
    posicoes=[]
    for i in range(10):
        if numeros[i] == pesquisa:
            posicoes.append(i+1)
    return str(posicoes)

numeros_introduzido=[]
for i in range(10):
    numero_introduzido=int(input("Introduza 10 numeros inteiros: "))
    numeros_introduzido.append(numero_introduzido)

numero_pesquisa=int(input("Introduza um numero para procrurar na lista: "))

print(f"O número {numero_pesquisa} está nas posições: {search_number(numeros_introduzido,numero_pesquisa)}")