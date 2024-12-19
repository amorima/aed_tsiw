'''
Implemente um programa que peça ao utilizador a indicação de 2 números inteiros (limite inferior e limite superior), calculando em seguida a soma de todos os pares entre esse intervalo (incluindo os limites indicados.
Exemplo: Limite inferior: 1 Limite superior: 10 Soma dos pares no intervalo = 2+4+6+8+10=30 
'''

limiteInferior=int(input("Indique o limite Inferior: "))
limiteSuperior=int(input("Indique o limite Superior: "))

if limiteInferior > limiteSuperior:
    print("O limite inferior tem de ser menor que o limite superior")
    exit()

todosNumeros=list(range(limiteInferior,limiteSuperior+1))
numerosPar = [i for i in todosNumeros if i % 2 == 0]

soma=sum(numerosPar)

print(f"A soma de todos os pares entre {limiteInferior} e {limiteSuperior} é {soma}")