'''Implemente a função romanNumeral que receba um número entre 1 e 999 (pedido ao utiliza-
dor) e devolva o mesmo valor em numeração Romana '''

import os

# Limpa a consola
os.system("cls")


def roman_numeral(numero):
    """a função romanNumeral que recebe um número entre 1 e 999 (pedido ao utilizador) e devolva o mesmo valor em numeração Romana

    Args:
        numero (str): número entre 1 e 999

    Returns:
        str: o mesmo valor em numeração Romana
    """
    primeiro_numero=0
    segundo_numero=0
    terceiro_numero=0
   
    def unidades(numero):
        '''
        Retorna o valor das unidades em numeração romana
        '''
        if numero == "1":
            primeiro_numero="I"
        elif numero == "2":
            primeiro_numero="II"
        elif numero == "3":
            primeiro_numero="III"
        elif numero == "4":
            primeiro_numero="IV"
        elif numero == "5":
            primeiro_numero="V"
        elif numero == "6":
            primeiro_numero="VI"
        elif numero == "7":
            primeiro_numero="VII"
        elif numero == "8":
            primeiro_numero="VIII"
        elif numero == "9":
            primeiro_numero="IX"
        elif numero == "0":
            print("Número Inválido")
        return primeiro_numero

    def dezenas(numero):
        '''
        Retorna o valor das dezenas em numeração romana
        '''
        if numero == "1":
            segundo_numero="X"
        elif numero == "2":
            segundo_numero="XX"
        elif numero == "3":
            segundo_numero="XXX"
        elif numero == "4":
            segundo_numero="XL"
        elif numero == "5":
            segundo_numero="L"
        elif numero == "6":
            segundo_numero="LX"
        elif numero == "7":
            segundo_numero="LXX"
        elif numero == "8":
            segundo_numero="LXXX"
        elif numero == "9":
            segundo_numero="XC"
        elif numero == "0":
            return
        return segundo_numero

    def centenas(numero):
        '''
        Retorna o valor das centenas em numeração romana
        '''
        if numero == "1":
            terceiro_numero="C"
        elif numero == "2":
            terceiro_numero="CC"
        elif numero == "3":
            terceiro_numero="CCC"
        elif numero == "4":
            terceiro_numero="CD"
        elif numero == "5":
            terceiro_numero="D"
        elif numero == "6":
            terceiro_numero="DC"
        elif numero == "7":
            terceiro_numero="DCC"
        elif numero == "8":
            terceiro_numero="DCCC"
        elif numero == "9":
            terceiro_numero="CM"
        return terceiro_numero
    if len(numero)==1:
        return unidades(numero)
    elif len(numero)==2:
        if numero[1]=="0":
            numero_romano=f"{dezenas(numero[0])}"
            return numero_romano
        else:
            numero_romano=f"{dezenas(numero[0])}{unidades(numero[1])}"
        return numero_romano
    elif len(numero)==3:
        if numero[1]=="0" and numero[2]=="0":
            numero_romano=f"{centenas(numero[0])}"
            return numero_romano
        elif numero[2]=="0":
            numero_romano=f"{centenas(numero[0])}{dezenas(numero[1])}"
            return numero_romano
        if numero[1]=="0":
            numero_romano=f"{centenas(numero[0])}{unidades(numero[2])}"
            return numero_romano
        numero_romano=f"{centenas(numero[0])}{dezenas(numero[1])}{unidades(numero[2])}"
        return numero_romano
    else:
        return print("Número Inválido")


# Solicita o input do utilizador
numero = input("Indique um número de 1-999: ")
print(roman_numeral(numero))