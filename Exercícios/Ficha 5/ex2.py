'''
Elabore um programa com o seguinte menu inicial: 
▪ Inicializar matriz: deve pedir ao utilizador a dimensão da matriz (nº de linhas /co-
lunas da matriz) e invocar uma função que preencha a matriz com valores aleató-
rios entre 10 e 100. A função deve imprimir a matriz gerada. 
 
▪ Matriz transposta: deve invocar uma função que receba a matriz gerada, e im-
prima a sua transposta 
 
▪ Maior valor: deve invocar uma função que receba a matriz e imprima o maior va-
lor da matriz 

▪ Sair : deve terminar o seu programa
'''
import os
import sys
import random

os.system("cls")

menu=1

def menu_screen():
    """Mostra o menu de opções
    """
    print("\tMENU")
    print("1 - Inicializar matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior Valor")
    print("0 - Sair")

def matrix_creator():
    """Pede o tamanho da matriz e insere valores aleatorios em cada um dos seus espaços
    """
    global lines
    global columns
    global matrix
    lines=0
    columns=0
    matrix=[]
    lines=int(input("Quantas linhas terá a matriz? "))
    columns=int(input("Quantas colunas terá a matriz? "))
    for i in range(lines):
        matrix.append([])
        for c in range(columns):
            number=random.randint(10,100)
            matrix[i].append(number)
    print()
    print("Matriz Gerada\n")
    for i in range(len(matrix)):
        for c in range(len(matrix[i])):
            print(matrix[i][c], end=" ")
        print()

def matrix_trans():
    """Faz a transposta da matriz da função matrix_creator
    """
    print()
    print("Matriz Original\n")
    for i in range(len(matrix)):
        for c in range(len(matrix[i])):
            print(matrix[i][c], end=" ")
        print()
    print()
    print("Matriz Transposta\n")
    for i in range(len(matrix)):
        for c in range(len(matrix[i])):
            print(matrix[c][i], end=" ")
        print()

def matrix_bigger():
    """Encontra e imprime o maior valor da matriz
    """
    biggest=max(max(lines) for lines in matrix)
    print(f"\nO maior valor da matriz é {biggest}")

def close_program():
    """Função que fecha o programa
    """
    os.system("cls")
    print("A encerrar o programa...")
    sys.exit()


menu_screen()
print()
menu=int(input("Escolha uma das opções: "))

while True:
    if menu == 1:
        os.system("cls")
        menu_screen()
        print()
        matrix_creator()
        menu=int(input("\nEscolha uma das opções: "))
    elif menu == 2:
        os.system("cls")
        menu_screen()
        print()
        matrix_trans()
        menu=int(input("\nEscolha uma das opções: "))
    elif menu == 3:
        os.system("cls")
        menu_screen()
        print()
        matrix_bigger()
        menu=int(input("\nEscolha uma das opções: "))
    elif menu == 0:
        close_program()
    else:
        os.system("cls")
        menu_screen()
        print()
        print("Opção inválida! Por favor selecione outra opção!")
        menu=int(input("\nEscolha uma das opções: "))