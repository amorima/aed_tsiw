'''Escreva um programa que leia um número inteiro e determine se esse número é par ou ímpar.'''

numero=int(input("Introduza um número: "))
calculo=int(numero % 2)

match calculo:
    case 0:
        print(f'O numero {numero} é par')
    case 1:
        print(f'O numero {numero} é impar')