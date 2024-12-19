'''O índice de massa corporal (IMC) de um indivíduo é obtido dividindo-se o seu peso (em Kg) pela sua altura (em m) ao quadrado. 
Assim, por exemplo, uma pessoa de 1,67m e pesando 55kg tem IMC igual a 19,72.
Implemente um simulador de índice de massa corporal (versão 1.0), pedindo ao utilizador a indicação do seu peso(em kg)
e da sua altura (em metros). Calcule o respetivo índice de massa corporal (IMC) e apresente-o com 2 casas decimais. '''

peso=float(input("Peso (kg): "))
altura=float(input("Altura (m): "))
imc=peso/(pow(altura,2))
print("O seu IMC é: {:.2f}" .format(imc))