'''
Implemente a função heartRate(fc) que receba a frequência cardíaca  de um indivíduo durante o treino, e que devolva (return) o nível de esforço efetuado, de acordo com as seguintes condições: 
• fcentre [50-80] – treino aeróbico 
• Fcentre ]80-100] – treino cardiovascular 
• Fcentre ]100-120] – treino aeróbico ideal 
• Fcentre ]120-100] – treino anaeróbico
'''

def heartRate(fc:int):
    """
    determina o esforço efetuado em treino, em função da fc
    Arg: fc: inteiro
    """
    if fc >= 50 and fc <=80:
        return "Treino Aeróbico"
    elif fc > 80 and fc <=100:
        return "Treino Cardiovascular"
    elif fc > 100 and fc <=120:
        return "Treino aeróbico ideal"
    elif fc > 120 and fc <=140:
        return "Treino anaeróbico"
    else:
        return "Treino Mortal"


print(heartRate(125))
print(heartRate(34))
print(heartRate(150))