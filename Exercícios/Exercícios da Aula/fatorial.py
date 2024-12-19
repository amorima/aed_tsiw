'''
Elabore um programa que simule a função fatorial, isto é, que leia um número e determine o fatorial desse número.
Exemplo: Fatorial de 5 = 5 * 4 * 3 * 2 * 1 = 120 Note que 0! = 1 
Nota: não utilizar a função math.factorial() O objetivo é desenvolvermos a nossa própria função fatorial!
'''

numeroInicial = int(input("Indique o um número: "))
numeroBuffer=numeroInicial
fatorial=numeroInicial

while numeroInicial >1:
    numeroInicial-=1
    fatorial*=(numeroInicial)

print(f"O fatorial de {numeroBuffer} é {fatorial}")