'''Adapte o simulador de índice de massa corporal (IMC) desenvolvido no ponto
4. Depois de calcular e imprimir o IMC, o seu programa deve categorizar o
indivíduo, em função do índice de IMC obtido, e de acordo com a seguinte
imagem:'''

peso=float(input("Peso (kg): ")) #Input de peso
altura=float(input("Altura (m): ")) #input de altura
imc=float(peso/(pow(altura,2))) #cálculo do IMC
print("O seu IMC é: {:.2f}" .format(imc)) #print da informação do IMC

#Filtragem da resposta
if imc < 18.5:
    print("Baixo Peso")
elif 18.5 <= imc <= 24.9:
    print("Peso Normal")
elif 25 <= imc <= 29.9:
    print("Excesso de Peso")
elif 30 <= imc <= 34.9:
    print("Obesidade Grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Mórbida")