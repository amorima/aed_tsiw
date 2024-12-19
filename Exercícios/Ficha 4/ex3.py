'''
Crie um programa que leia a pontuação de 10 participantes num concurso de progra-
mação (a pontuação deve estar validada entre 0 a 20, por uma estrutura try-except).  
 
O programa deve invocar uma função, positiveList que receba a lista das 10 pontua-
ções e devolva uma nova lista apenas com as pontuações positivas (>=10).
'''

import os
import random

# Limpa a consola
os.system("cls")

def positive_list(pontuacoes):
    pontuacoes_positivas=[]
    resultado=""
    for i in pontuacoes:
        if i < 1 and i > 20:
            break
        elif i >= 10:
            pontuacoes_positivas.append(i)
    resultado=f"Pontuações positivas: {pontuacoes_positivas}"
    return resultado

pontuacoes=[]
try:
    while len(pontuacoes) < 10: #pede que o utilizador introduza 10 números inteiros
        numero_introduzido=int(input((f"Introduza o número {len(pontuacoes)+1} de 10: ")))
        if numero_introduzido > 0 and numero_introduzido <= 20:
            pontuacoes.append(numero_introduzido)
        else:
             raise Exception
except:
     print("Introduza um número entre 1 e 20")
     exit()
print("\n")
print(positive_list(pontuacoes))
