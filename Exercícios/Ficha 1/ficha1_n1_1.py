'''Crie um conversor que leia uma temperatura em ºCelsius e imprima a temperatura equivalente em º Fahrenheit (com 2 casas decimais).
Fórmula de conversão: ºF = 1.8 * ºC + 32 '''

Celsius=float(input("Temperatura em º Celsius: ")) #Pede para introduzir os graus em Celsius
Fahrenheit=1.8*Celsius+32 #Fórmula para calcular os graus em Fahrenheit, com base nos graus Celsius

print("Temperatura em º Farrenheit: {:.2f}" .format(Fahrenheit)) #Mostra a temperatura convertida