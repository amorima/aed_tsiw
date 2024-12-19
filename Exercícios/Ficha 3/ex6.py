'''
 Elabore a função standardName(nome) que deve receber um nome completo (em 
resultado de um input)e devolve uma string com o nome normalizado: inclui 
o primeiro e o último nome (tal como no exercício anterior) e abreviaturas 
de todos os outros nomes intercalares. 
 
Exemplo: 
standardName(‘Carlos Alberto Costa Pereira’)    => Carlos A. C. Pereira
'''

import os

# Limpa a consola
os.system("cls")

def standard_name(nome):
    '''A função standard_name(nome) recebe um nome completo e devolve uma string com o nome normalizado'''
    # Divide o nome completo em palavras
    partes = nome.split()
    
    # Primeiro nome e último nome
    primeiro_nome = partes[0]
    ultimo_nome = partes[-1]
    
    # Cria as iniciais dos nomes do meio
    iniciais = [f"{parte[0]}." for parte in partes[1:-1]]
    
    # Constrói o nome normalizado
    nome_abreviado = f"{primeiro_nome} {' '.join(iniciais)} {ultimo_nome}"
    return nome_abreviado

# Solicita o input do utilizador
nome = input("Indique um nome completo: ")
print(standard_name(nome))