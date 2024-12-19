'''
Implemente um programa que leia um número (entre 1 e 99) e determine a
sua representação em linguagem binária.
'''

import os #importa a libraria operative system
os.system("cls") #limpa a consola

numero_inserido=int(input("Insira um número entre 1 e 99: "))
print("\n\n")
divisao=numero_inserido
binario=[]
if numero_inserido < 1 or numero_inserido > 99:
    print("ERRO! Por favor introduza um número entre 1 e 99\n\n")
    exit()

while divisao > 0:
    resto=divisao%2
    divisao=int(divisao/2)
    binario.append(resto)

binario.reverse()
print(*binario, sep=' ')
print("\n\n")