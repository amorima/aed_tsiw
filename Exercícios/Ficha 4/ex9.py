'''
Implemente um programa que permita ler o número de visitantes numa exposição, que 
decorre de Domingo a Sábado.  
O seu Em seguida elabore uma função que permita listar o número de visitantes diário 
por ordem decrescente, tal como na imagem abaixo apresentada. 
Indique ainda, no final, o número médio de visitantes por dia (com 2 casas decimais) e 
o dia que mais se aproximou do número médio de visitantes.
'''
import os

os.system("cls")

def exposi(dias_semana, visitantes):
    os.system("cls")
    media_visitantes=sum(visitantes)/len(visitantes)
    lista=list(zip(visitantes, dias_semana))
    lista.sort()
    for vis, dias in lista:
        print(f"{dias}       {vis}")
    mais_proximo=visitantes
    mais_proximo=[x-media_visitantes for x in mais_proximo]
    mais_proximo_fim=mais_proximo.index(min(mais_proximo))
    print(mais_proximo)
    print(mais_proximo_fim)
    print(mais_proximo.index(min(mais_proximo)))
    print("\n")
    print(f"Número médio de visitas diárias: {media_visitantes:.2f}")
    print(f"Dia mais próximo do valor médio: {lista[mais_proximo_fim]}")


dias_semana=["Domingo: ", "Segunda: ", "Terça:   ", "Quarta:  ", "Quinta:  ", "Sexta:   ", "Sábado:  "]
visitantes=[]
for i in dias_semana:
    entrada=int(input(f"{i}        "))
    visitantes.append(entrada)

exposi(dias_semana, visitantes)