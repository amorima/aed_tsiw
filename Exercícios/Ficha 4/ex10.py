'''
Elabore um programa que permita gerir uma fila de espera (como num supermercado, 
ou num serviço de atendimento) com capacidade máxima para 20 lugares.  
Quando o programa se inicia, todos os lugares da fila devem estar livres. 
Layout da fila de espera (lista com 20posições):
'''

import os
os.system("cls")

def ticket():
    if fila.count("L") == 0: # Verifica se a fila está completa
        print("Fila completa")
    else:
        if fila.count("O") == 0: # Verifica se já há "O" na fila
            posicao = fila.index("L")
        else:
            fila.reverse() # Inverte a lista para encontrar a última posição ocupada por "O"
            posicao_dois = fila.index("O")
            fila.reverse()  # Reverte a lista de volta ao estado original

            posicao = len(fila) - 1 - posicao_dois # Calcula a posição correta na lista original
            posicao += 1 # Definir a posição final como o próximo lugar livre após o último "O"

        fila[posicao] = "O" # Atualiza a posição na fila com "O" e informa a posição ocupada
        print(f"Está na {posicao + 1}ª posição da fila de espera.\n")


def atendimento():
    posicao=fila.index("O") #Encontra a primeira posição onde a senha está tirada
    print(f"A senha {posicao+1} será atendida.\n") #Imprime a posição da senha
    fila[posicao]="L" #Transforma num espaço livre

def estado(fila):
    livres=fila.count("L") #conta o numero de senhas livres
    ocupados=fila.count("O") #conta o numero de senhas ocupadas
    print(f"Número de lugares ocupados:{ocupados}\nNúmero de lugares livres: {livres}")


fila=["L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L", "L"]

menu="S"

while True: 
    if menu=="S": #Mostra o menu quando munu é igual a S
        os.system("cls")
        print("\tMENU\n\n1 - Tirar Ticket\n2 - Atendimento\n3 - Estado da fila de espera \n0 - Sair\n\n")
        menu=int(input("Selecione uma opção: "))
        while True: #Loop para ir para as opções selecionadas e executar as respetivas funções
            if menu == 1:
                os.system("cls")
                ticket()
                menu=input("\nDeseja voltar ao menu inicial? S/N: ")
                menu=menu.upper()
                if menu == "S":
                    break
                else:
                    os.system("cls")
                    exit
            elif menu == 2:
                os.system("cls")
                atendimento()
                menu=input("\nDeseja voltar ao menu inicial? S/N: ")
                menu=menu.upper()
                if menu == "S":
                    break
                else:
                    os.system("cls")
                    exit
            elif menu == 3:
                os.system("cls")
                estado(fila)
                menu=input("\nDeseja voltar ao menu inicial? S/N: ")
                menu=menu.upper()
                if menu == "S":
                    break
                else:
                    os.system("cls")
                    exit
            elif menu == 0:
                os.system("cls")
                exit