"""
Pretende-se desenvolver um programa que permita
ler/consultar os dados registados no ficheiro temperatura.
txt, ficheiro esse que contém dados devolvidos
pela leitura de um sensor de temperatura!
"""

import os

def ficheiro_existe():
    """Verifica se o ficheiro existe no filepath, caso não exista cria-o
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="utf-8"):
            pass

def consulta_por_data():
    """Consulta e filtra pela data fornecida
    """
    verificar=input("Introduza uma data no formato AAAA-MM-DD: ").strip()
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
        os.system("cls")
        print(f"Data{17*" "}Hora{17*" "}Temperatura")
        print(f"{57*"-"}")
        for linha in linhas:
            if verificar in linha:
                linha_final=linha.split(";")
                print(f"{linha_final[0]}{9*" "}{linha_final[1]}{19*" "}{linha_final[2]}", end="")
    input()

def consulta_estatistica():
    """Encontra o valor de temperatura mínimo, máximo e médio
    """
    temperaturas=[]
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
        os.system("cls")
        for linha in linhas:
            linha_final=linha.split(";")
            temperaturas+=linha_final[2].strip().split()
        for i in range(len(temperaturas)):
            temperaturas[i] = int(temperaturas[i])
    print(f"Temperatura mínima      : {min(temperaturas)}")
    print(f"Temperatura máxima      : {max(temperaturas)}")
    print(f"Temperatura média       : {sum(temperaturas)/len(temperaturas)}")
    input()

#----INICIO DO PROGRAMA----
""" Abre um ficheiro.txt """

nome_ficheiro="temperatura.txt"
file_path= ".\\files\\"+nome_ficheiro

menu_opcao="1"
while menu_opcao != "0":
    os.system("cls")
    ficheiro_existe()
    print("\t MENU")
    print("1 - Consulta por data")
    print("2 - Consulta estatística")
    print("0 - Sair")
    print("\n")
    menu_opcao=input("\tOpção: ")
    if menu_opcao == "1":
        consulta_por_data()
    elif menu_opcao == "2":
        consulta_estatistica()
