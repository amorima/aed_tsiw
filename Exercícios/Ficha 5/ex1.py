'''Elabore um programa que leia os dados de uma 
matriz 3x3 de inteiros: no fundo, deve ler dados 
para uma lista que contém 3 sub-listas, cada 
uma delas com 3 elementos. 
Em seguida implemente uma função invert que 
receba a matriz lida e a imprima, assim como à 
sua transposta. 
 Nota: matriz transposta consiste e trocar as “li-
nhas” pelas “colunas” da matriz.'''

import os

os.system("cls")

matrix=[]
lines=3
columns=3

for i in range(lines):
    matrix.append([])
    for c in range(columns):
        number=int(input("Número: "))
        matrix[i].append(number)

print(matrix)

for i in range(len(matrix)):
    for c in range(len(matrix[i])):
        print(matrix[i][c], end=" ")
    print()

'''for lines in matrix:
    print(lines)'''