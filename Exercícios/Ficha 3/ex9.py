'''
 Implemente a função printCharLine(texto,numeroCar) que receba dois argumentos: um texto e o nº de caracteres que se pretende imprimir por cada linha. 
 A sua função deve imprimir o texto em função desse nº de caracteres
'''

import os

# Limpa a consola
os.system("cls")

def print_char_line(texto,numero_car):
    """recebe dois argumentos: um texto e o nº de caracteres que se pretende imprimir por cada linha.

    Args:
        texto (str): texto a separar por linhas
        numero_car (int): Numero de caracteres por linha

    Returns:
        str: Texto separado por linhas
    """
    tamanho=len(texto)
    numero_car_ant=int(numero_car)
    numero_car_in=int(numero_car)
    texto_dividido=""
    contador=0
    while (tamanho/numero_car) >= contador:
        inicio=int(numero_car_in-numero_car_ant)
        texto_dividido+=f"{texto[inicio:numero_car_in]}\n"
        inicio+=numero_car
        numero_car_in+=numero_car
        contador+=1
    return texto_dividido

# Solicita o input do utilizador
texto = input("Indique um texto: ")
numero_car = int(input("Indique o número de caracteres: "))
print(print_char_line(texto,numero_car))