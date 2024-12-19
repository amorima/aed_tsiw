'''
 Escreva a função removeSpaces(texto) que receba um texto e substitua as 
sequências de dois ou mais espaços por um único espaço. A função deve 
imprimir o texto resultante.
'''
def remove_spaces(texto):
    '''removeSpaces(texto) recebe um texto e substitui as sequências de dois ou mais espaços por um único espaço.'''
    lista_nomes=texto.split(" ")
    for palavras in lista_nomes:
        if palavras == "":
            continue
        print(palavras, end=" ")

texto=str(input("Indique um texto: "))
remove_spaces(texto)