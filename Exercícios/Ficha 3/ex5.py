'''
Escreva a função shortName(nome) que deve receber um nome completo (em resultado de um input)e devolve uma string com o primeiro e último nome (primeiro nome próprio e último apelido).
Exemplo: shortName(‘Manuel Jorge da Costa Pereira’) => Manuel Pereira
'''

import os

# Limpa a consola
os.system("cls")

def short_name(nome):
    '''Recebe um nome completo (em resultado de um input)e devolve uma string com o primeiro e último nome'''
    tamanho=len(nome)
    primeiro_espaço=nome.index(" ")
    ultimo_espaco=nome.rfind(" ")
    primeiro_ultimo_nome=(nome[0:primeiro_espaço],nome[ultimo_espaco+1:tamanho])
    return primeiro_ultimo_nome

nome=str(input("Indique um texto: "))
print(*short_name(nome))