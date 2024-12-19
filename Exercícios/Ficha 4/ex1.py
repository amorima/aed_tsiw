'''
Elabore  a  função aboveAverage  que  receba  uma  lista  com  10  números  inteiros  (nú-
mero inseridos pelo utilizador) e que devolva quantos desses números estão acima da 
média.
'''
import os

# Limpa a consola
os.system("cls")

def above_average(numeros):
    """Retorna a quantidade de numeros acima da média dos números introduzidos pelo utilizador.

    Args:
        numeros (int): Lista de números inteiros introduzida pelo utilizador
    """
    contador=0
    media=sum(numeros)/10 #calcula a media da lista de numeros introduzida pelo utilizador
    for i in numeros:
        if i > media: #conta os numeros acima da media
            contador+=1
    return(contador)

numeros=[]
while len(numeros) < 10: #pede que o utilizador introduza 10 números inteiros
    numero_introduzido=int(input((f"Introduza o número {len(numeros)+1} de 10: ")))
    numeros.append(numero_introduzido)
print("\n")
print(f"Existem {above_average(numeros)} números acima da média")