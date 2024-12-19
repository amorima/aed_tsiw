"""
Implemente uma função designada maior que receba n números inteiros positivos (n é variável, dependendo dos argumentos fornecidos à função) A função deve devolver (return) o maior desses números 
"""

def maior(*numeros):
    """
    Recebe uma lista de numeros inteiros, devolvendo o maior deles
    Args: numeros inteiros
    """
    maximo=numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros [i]
    return maximo

maximo=maior(3,10,5,25,80,1345)
print(maximo)