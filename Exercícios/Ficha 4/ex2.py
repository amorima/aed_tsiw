"""
Elabora uma função generateNumbers que permita gerar uma chave do Euromilhões 
de forma aleatória (5 números inteiros entre 1 e 50), assim como as estrelas (duas es-
trelas entre 1 e 12).  
A função generateNumbers deve ter 3 argumentos de entrada: limite inferior, limite 
superior, e quantidade de números a gerar. Por exemplo, para gerar chaves do Euromi-
lhões, deve invocar a função com os seguintes argumentos: 
generateNumbers(1,50, 5)   -> gera 5 números entre 1 e 50 
generateNumbers(1,12,2)    -> gera 2 números entre 1 e 12 (estrelas) 
 
A função deve devolver uma lista com os números gerados. Obviamente que a função 
não pode devolver números nem estrelas repetidas! 
 
No final imprima a chave gerada e pergunte ao utilizador se pretende gerar nova chave 
(S/N).
"""

import os
import random

# Limpa a consola
os.system("cls")

def generate_numbers(limite_inferior, limite_superior, quantidade):
    return random.sample(range(limite_inferior, limite_superior+1), quantidade)

while True:
    os.system("cls")
    #calculo dos numeros
    numeros=generate_numbers(1, 50, 5)
    estrelas=generate_numbers(1, 12, 2)

    print(f"Chave do Euromilhões \n Números: {numeros} \t Estrelas: {estrelas}")

    print("\n")
    chave=input("Deseja gerar nova chave? (S/N):")
    print("\n\n")

    if chave.upper() == "S":
        continue
    else:
        exit()