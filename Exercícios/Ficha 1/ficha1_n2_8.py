'''Escreva um programa que implemente um simulador do peso ideal (versão 2.0!).
O algoritmo deve pedir ao utilizador o sexo (M para masculino e F para
feminino) e a altura (em cm).
A simulação do peso ideal é dada pela seguinte formula:
Peso ideal = (h-100) - (h-150)/k
Sendo que:
k = 2 para o sexo feminino e k = 4 para o sexo masculino;
h é a altura em cm'''

sexo=str(input("Indique o sexo (M/F): ")) #introdução dos valores para a variável sexo
altura=float(input("Altura em cm: ")) #introdução dos valores para a variável altura

match sexo: #Compara o input do sexo e calcula o peso ideal
    case "M":
        pesoIdeal=float((altura-100)-((altura-150)/4))
        print(f"O peso ideal é: {pesoIdeal} Kg")
    case "F":
        pesoIdeal=float((altura-100)-((altura-150)/2))
        print(f"O peso ideal é: {pesoIdeal} Kg")
    case _: #caso seja inserido um valor diferente de M e F na variavel sexo
        print("Sexo desconhecido")