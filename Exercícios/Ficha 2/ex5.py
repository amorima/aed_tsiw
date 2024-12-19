'''
Elabore um programa que leia um número (inteiro e positivo) e indique se ele é primo ou não. Nota: Um número primo é divisível apenas por si próprio e por 1. 
'''
import os
os.system("cls")

print("\tVERIFICADOR DE NÚMEROS PRIMOS")

contador=2
resto_dif_zero=0

numero_inserido=int(input("\n\n\t\tInsira um número: "))
if numero_inserido < 0:
    print("Insira um número inteiro e positivo")

while contador < numero_inserido:
    if (numero_inserido % contador) != 0:
        resto_dif_zero+=1
    contador+=1

if resto_dif_zero == (numero_inserido-2):
    print(f"\n\n\t\t\tO número {numero_inserido} é primo\n\n")
else:
    print(f"\n\n\t\t\tO número {numero_inserido} não é primo\n\n")