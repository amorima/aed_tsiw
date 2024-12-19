'''Crie um conversor de segundos em horas/minutos/segundos.  Deve solicitar ao utilizador a indicação de um
determinado número de segundos.  Em seguida converte esse valor de segundos no número correspondente de horas, 
minutos e segundos, conforme ilustram os seguintes exemplos: 
7300 segundos = 2 horas, 1 minutos, 40 segundos 
8054 segundos = 2 horas, 14 minutos, 14 segundos '''

inputSegundos=int(input("Indique o tempo em segundos: "))
horas=float(inputSegundos/3600)
minutos=(horas-int(horas))*60
segundos=(minutos-int(minutos))*60

print(f"{int(horas)} horas, {int(minutos)} minutos, {int(segundos)} segundos")