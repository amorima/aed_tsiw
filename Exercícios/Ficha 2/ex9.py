"""
Leia um conjunto de n números inteiros (sendo n indicado previamente
pelo utilizador). Em seguida determine o segundo maior valor de entre o
conjunto de números lido.
"""

import os
import random

# Limpa a consola
os.system("cls")

# Lê quantos números o utilizador deseja gerar
numero_inserido = int(input("Quantos números deseja ler?: "))

# Inicializa as variáveis para o maior e o segundo maior
maior = 0
segundo_maior = 0

# Conta quantos números já foram processados
contador = numero_inserido

# Gera os números aleatórios e encontra o maior e o segundo maior
while contador > 0:
    numero_atual = random.randint(1, 99)
    print(f"Número: {numero_atual}")
    
    # Verifica se o número atual é maior que o maior número encontrado até agora
    if numero_atual > maior:
        segundo_maior = maior  # Atualiza o segundo maior para o valor anterior de maior
        maior = numero_atual  # Atualiza o maior número
    elif numero_atual > segundo_maior and numero_atual != maior:
        # Se o número atual não for o maior, verifica se é maior que o segundo maior
        segundo_maior = numero_atual
    
    contador -= 1

# Exibe o resultado
print(f"\n\n\t\tO segundo maior valor da lista de números lidos é: {segundo_maior}")