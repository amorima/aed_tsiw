'''
Implemente a função countText(texto). A função deve receber um texto, 
inserido através de um input, e deve imprimir:  
• Número de caracteres 
• Número de espaços 
• Número de vogais 
Incluídos nesse texto.
'''

def count_text (texto):
    """Recebe um texto e imprime o número de caracteres, espaços e vogais.

    Args:
        texto (str): texto em que vão ser contados os caracteres, espaços e vogais
    """
    texto=texto.lower()
    print("Número de Caracteres: ", len(texto))
    print("Número de vogais: ", (texto.count("a")+texto.count("e")+texto.count("i")+texto.count("o")+texto.count("u")))
    print("Número de espaços: ", texto.count(" "))

texto=str(input("Indique um texto: "))
count_text(texto)



