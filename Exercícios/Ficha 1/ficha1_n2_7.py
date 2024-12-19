'''Implemente um programa que funcione como um pequeno simulador de esforço
cardíaco, quando um atleta desenvolve atividade física.'''

sexo=str(input("Indique o Sexo (M/F): ")) #introdução dos valores para a variável sexo
idade=float(input("Indique a idade: ")) #introdução dos valores para a cariável idade
fcmM=int(220-idade) #cálculo do FCM para o sexo masculino
fcmF=int(226-idade) #cálculo do FCM para o sexo feminino

if sexo.upper() == "F" :
    print(f"FCM= {fcmF} bpm") #caso o utilizador tenha inserido F exibe os valores calculados para o sexo feminino
elif sexo.upper() == "M" :
    print(f"FCM= {fcmM} bpm") #caso o utilizador tenha inserido M exibe os valores calculados para o sexo masculino
else:
    print("Introduza apenas M ou F") #caso o utilizador tenha inserido outro valor diferente de M ou F exibe este erro