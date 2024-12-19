'''Escreva um pequeno programa que calcule o seu peso ideal!
Existem inúmeras fórmulas para determinar o peso ideal de uma pessoa, dependendo do sexo, altura, idade, estrutura óssea, etc.
Neste exercício vamos usar (para já!) um algoritmo de cálculo simplificado, baseado apenas na sua altura, de acordo com a fórmula:
Peso ideal = (altura-100) * 0.9 Apresente o resultado com uma casa decimal, como no exemplo abaixo.'''

altura=float(input("Altura em cm: "))
pesoIdeal=(altura-100)*0.9

print("O seu Peso Ideal: {:.1f}" .format(pesoIdeal))