'''Elabore um programa que leia uma lista de 10 números inteiros.  
Em seguida, dado um determinado valor de pesquisa, invoque a função searchNum-
ber(lista, pesquisa) que deve devolver as posições em que encontra o valor de pesquisa, 
na lista.  
Caso o valor de pesquisa não exista na lista, deve surgir uma mensagem adequada.'''

import os

os.system("cls") # Limpa a consola

def pluvio(meses, pluviosidade):
    """Importa a lista de meses e de pluviosidades, reorganiza os mesmos de maior para menor e devolve uma lista com mês e valor

    Args:
        meses (str): lista de meses
        pluviosidade (int): lista de pluviosidades
    """
    dados = list(zip(pluviosidade, meses))# Combinar as listas em tuplos (pluviosidade, mês)
    dados.sort(reverse=True)# Ordenar a lista de tuplos com base na pluviosidade em ordem decrescente
    for pluv, mes in dados:# Imprimir os dados ordenados
        print(f"{mes}: {pluv}")


meses=["Janeiro   ", "Fevereiro ", "Março     ", "Abril     ", "Maio      ", "Junho     ", "Julho     ", "Agosto    ", "Setembro  ", "Outubro   ", "Novembro  ", "Dezembro  "] #lista de meses
pluviosidade=[]

for i in range(12): #loop para guardar a pluviosidade mensal numa lista
    valor=int(input(f"Pluviosidade no mês de {meses[i]}: "))
    pluviosidade.append(valor)

print("\n\n")
pluvio(meses,pluviosidade)