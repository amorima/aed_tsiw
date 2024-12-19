'''
Crie uma aplicação que permita gerir um ficheiro de países 
(paises.txt), com uma estrutura semelhante à apresentada 
no exemplo: país;continente
'''

import os

def ficheiro_existe():
    """Verifica se o ficheiro existe no filepath, caso não exista cria-o
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="utf-8"):
            pass

def inserir_paises():
    """Pede para inserir os paises
    """
    pais=input("País       : ").strip()
    continente=input("Continente : ").strip()
    linha=f"{pais}{(27-len(pais))*" "}{continente}\n"
    with open(file_path, "r+", encoding="utf-8") as ficheiro:
        list=ficheiro.read()
        if list.find(pais)!=-1:
            print(f"O país '{pais}' já existe e não será duplicado!")
        else:
            ficheiro.write(linha)
    input()

def consulta_paises():
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        file=ficheiro.readlines()
        os.system("cls")
        print(f"Pais{22*" "}Continente")
        print(f"{38*"-"}")
        for line in file:
            print(line.strip())
    input()

def consulta_continente():
    continente = input("Continente: ").strip()
    print("\n")
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        file=ficheiro.readlines()
        os.system("cls")
        print(f"Pais{22*" "}Continente")
        print(f"{38*"-"}")
        for line in file:
            if line.find(continente)!=-1:
                print(line.strip())
    input()

def paises_por_continente():
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        file=ficheiro.readlines()
        os.system("cls")
        for cont in lista_continentes:
            quan_continentes=0
            for line in file:
                if line.find(cont)!=-1:
                    quan_continentes+=1
            print(f"{cont}: {quan_continentes}")
    input()


""" Início do programa """

nome_ficheiro="paises.txt"
file_path= ".\\files\\"+nome_ficheiro
os.system("cls")
lista_continentes=["Europa", "Asia", "America", "Africa", "Oceania"]
menu_opcao="1"
while menu_opcao != "0":
    os.system("cls")
    print("\t MENU")
    print("1 - Inserir Países")
    print("2 - Consulta Países")
    print("3 - Consulta por continente")
    print("4 - Consulta nº países")
    print("0 - Sair")
    print("\n")
    menu_opcao=input("\tOpção: ")
    if menu_opcao == "1":
        ficheiro_existe()
        inserir_paises()
    elif menu_opcao == "2":
        ficheiro_existe()
        consulta_paises()
    elif menu_opcao == "3":
        ficheiro_existe()
        consulta_continente()
    elif menu_opcao == "4":
        ficheiro_existe()
        paises_por_continente()

lista_continentes=()