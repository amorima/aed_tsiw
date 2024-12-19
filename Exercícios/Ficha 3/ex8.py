'''
Escreva a função reverseWords(texto) que receba um texto e devolva o 
mesmo texto, mas com as palavras por ordem inversa.
'''

import os

# Limpa a consola
os.system("cls")

def reverse_words(texto):
    '''
    Recebe um texto e devolva o mesmo texto, mas com as palavras por ordem inversa.
    Parametros:
    texto (str): texto
    Retorna:
    str: texto invertido
    '''
    texto_invertido=""
    palavras=texto.split()
    tamanho=len(palavras)
    while tamanho > 0:
        texto_invertido+=f"{palavras[tamanho-1]} "
        tamanho-=1
    return texto_invertido

# Solicita o input do utilizador
texto = input("Indique um texto: ")
print(reverse_words(texto))