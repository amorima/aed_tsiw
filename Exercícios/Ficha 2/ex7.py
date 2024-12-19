'''Escreva um programa que verifique se um determinado número (inteiro e
positivo) é perfeito.
'''
import os #importa a libraria operative system
os.system("cls") #limpa a consola

#Declaração de variáveis
numero_inserido=int(input("Indique um número: "))
contador=numero_inserido-1
divisor_proprio=[]

#Mostra mensagem de erro caso o número não seja inteiro e positivo
if numero_inserido < 0:
    print("Insira um número inteiro e positivo")

#Procura todos os divisores próprios do numero inserido
while contador > 0:
    if numero_inserido%contador==0:
        divisor_proprio.append(contador)
    contador-=1

#Verifica se a soma dos divisores próprios é igual ao numero inserido para inferir a resposta
if sum(divisor_proprio) == numero_inserido:
    print(f"O número {numero_inserido} é um número perfeito")
else:
    print(f"O número {numero_inserido} não é um número perfeito")