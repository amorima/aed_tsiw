'''
Implemente um programa que leia 10 número e no final indique o maior e a média.
Nota: se indicar um número superior a 20, o seu programa deve ignorá-lo!
'''
somaNumeros=0
i=0
maior=0

while i < 10:
    numero = int(input("Indique o {:n}º número: " .format(i+1)))
    if numero >20:
        continue
    somaNumeros+= numero
    i+=1
    if numero > maior:
        maior=numero

print(f"A média é {somaNumeros} e o número maior é {maior}")