'''
Elabore um programa que permita gerir a ocupação de um pequeno parque de estaciona-
mento, com o layout abaixo apresentado (3 filas de estacionamento, cada uma delas com 
5 lugares).
'''

import os
import sys

os.system("cls")

park=[["L", "L", "L", "L", "L"],
      ["L", "L", "L", "L", "L"],
      ["L", "L", "L", "L", "L"]]

def menu_screen():
    print("\tMENU")
    print("1 - Entrada de veículo")
    print("2 - Saída de veículo")
    print("3 - Estado do Parque")
    print("3 - Sair")

def car_in():
    for i in range(len(park)):
        for c in range(len(park[i])):
            if park[i][c] == "L":
                park[i][c] = "O"
                print(f"Por favor estacione na fila {i+1}, lugar {c+1}.")
                return
    print("O parque está cheio.")

def car_out():
    line=int(input("Digite em que fila está o seu veículo: "))
    column=int(input("Digite em que lugar está o seu veículo: "))
    park[line-1][column-1]="L"
    print("O lugar ficou livre")

def park_status():
    print(f"Quantidade de lugares ocupados: {sum(row.count("O") for row in park)}")
    print(f"Quantidade de lugares livres: {sum(row.count("L") for row in park)}")
    print("\n")
    for i in range(len(park)):
        for c in range(len(park[i])):
            print(park[i][c], end=" ")
        print()

def close_program():
    """Função que fecha o programa
    """
    os.system("cls")
    print("A encerrar o programa...")
    sys.exit()

menu_screen()
print("\n")
menu=int(input("Escolha uma das opções: "))

while True:
    if menu == 1:
        os.system("cls")
        menu_screen()
        print("\n")
        car_in()
        print("\n")
        menu=int(input("Escolha uma das opções: "))
    elif menu == 2:
        os.system("cls")
        menu_screen()
        print("\n")
        car_out()
        print("\n")
        menu=int(input("Escolha uma das opções: "))
    elif menu == 3:
        os.system("cls")
        menu_screen()
        print("\n")
        park_status()
        print("\n")
        menu=int(input("Escolha uma das opções: "))
    elif menu == 0:
        os.system("cls")
        print("A encerrar o programa...")
        sys.exit()
    else:
        os.system("cls")
        menu_screen()
        print()
        print("Opção inválida! Por favor selecione outra opção!")
        menu=int(input("\nEscolha uma das opções: "))