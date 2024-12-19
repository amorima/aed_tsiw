import os
import random

# Limpa a consola
os.system("cls")

def positive_list(pontuacoes,nomes):
    pontuacoes_positivas=[]
    nomes_positiva=[]
    resultado=""
    contador=0
    for i in pontuacoes:
        contador+=1
        if i < 1 and i > 20:
            break
        elif i >= 10:
            pontuacoes_positivas.append(i)
            nomes_positiva.append(nomes[contador-1])
    resultado=f"Nomes: {nomes_positiva} \nPontuações positivas: {pontuacoes_positivas}"
    return resultado

pontuacoes=[]
nomes=[]
try:
    while len(pontuacoes) < 10: #pede que o utilizador introduza 10 números inteiros
        numero_introduzido=int(input((f"Introduza o número {len(pontuacoes)+1} de 10: ")))
        if numero_introduzido > 0 and numero_introduzido <= 20:
            pontuacoes.append(numero_introduzido)
        else:
             raise Exception
    while len(nomes) < 10: #pede que o utilizador introduza 10 nomes
        nome_introduzido=str(input((f"Introduza o nome {len(nomes)+1} de 10: ")))
        nomes.append(nome_introduzido)
except:
     print("Introduza um número entre 1 e 20")
     exit()
print("\n")
print(positive_list(pontuacoes,nomes))