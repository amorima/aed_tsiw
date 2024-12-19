"""
Dado uma lista de N elementos (N deve ser pedido ao utilizador), crie uma função que 
ordene a lista e que permita gerar uma outra lista sem valores duplicados.
"""
import os
os.system("cls")

def elementos_ordenados(lista_elementos):
    lista_elementos = sorted(set(lista_elementos))  # Ordena e remove duplicados
    print(lista_elementos)

n_elementos=int(input("Insira a quantidade de elementos a ser inserido: "))
lista_elementos=[]

for i in range(n_elementos):  #Pede a introdução de N Elementos ao utilizador e guarda na lista_elementos
    elemento=int(input(f"Insira o {i+1}º elemento: "))
    lista_elementos.append(elemento)

elementos_ordenados(lista_elementos)
print("\n")