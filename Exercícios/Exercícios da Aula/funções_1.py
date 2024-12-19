'''
Implemente a função somatório que receba 2 números inteiros, como argumento de entrada. A função deve imprimir o somatório de todos os números inteiros incluídos nesse intervalo
'''

def soma (num1:int, num2:int):
    soma=0
    for i in range(num1, num2+1):
        soma+=i
    return(soma)

num1=int(input("Número 1: "))
num2=int(input("Número 2: "))
somatorio=soma(num1,num2)
print(somatorio)