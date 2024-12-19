'''
Considere no seu programa a seguinte lista de cidades:

cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']
 
Implemente um programa que leia a temperatura ocorrida em cada uma das cidades da lista acima definida. A temperatura de cada cidade deve ser um valor real situados entre [0-40].  Valide a introdução dos dados através de uma estrutura try-except.

Em seguida invoque a função dadosEstatistica(lista) que deve devolver o valor de temperatura mais distante da média e respetiva cidade onde ocorreu.   
'''

def dadosEstatistica(lista):
    '''
    recebe a listas das temperaturas, calcula a média e verifica qual o valor mais longe da média
    '''
    media=sum(lista)/len(lista)
    print(media)


cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia'] # lista de cidades

temperaturas=[]

while True:
    try:
        for i in cidades: # pede a introdução de das temperaturas para cada cidade e guarda na lista temperaturas
            input_temp=int(input(f"Insira a temperatura entre 0 e 40 para a cidade {i}: "))
            if input_temp >= 0 and input_temp <= 40:
                temperaturas.append(input_temp)
            else:
                raise
        if len(cidades) == len(temperaturas):
                    break
    except:
        print("Introduza valores válidos")

print(dadosEstatistica(temperaturas))