'''
Implemente a função invertText(texto). A função deve receber um texto 
(uma string),inserido através de um input, e deve imprimir o mesmo texto 
mas por ordem inversa.
'''
def invert_text(texto):
    caracteres=len(texto)
    for i in range(caracteres-1, -1, -1):
        print(texto[i], end="")


texto=str(input("Indique um texto: "))
invert_text(texto)