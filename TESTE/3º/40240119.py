# Número: 40240119
# Nome: António Amorim

'''
Pretende-se implementar um programa que permita analisar os resultados gerados por uma aplicação de running. Vamos imaginar que utilizamos uma aplicação de running para efetuar o tracking das atividades físicas (corrida). E que essa aplicação permite gerar um ficheiro: atividades.txt
'''

import os

def ficheiro_existe():
    """Cria novo ficheiro
    """
    with open(file_path, 'w', encoding="utf-8"):
        print("Progresso.txt criado com sucesso")
    
def consulta_distancia():
    """Pede para introduzir um 5k, 10k ou 21k, filtra e mostra os resultados correspondentes no ficheiro atividades.txt.
    """
    verificar=input("Introduza uma distância (5k, 10k ou 21k): ").strip()
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
        os.system("cls")
        print(f"Data{17*" "}Tempo Registado")
        print(f"{38*"-"}")
        for linha in linhas:
            if verificar in linha:
                linha_final=linha.split(";")
                return print(f"{linha_final[0]}{17*" "}{linha_final[2]}", end="")
    input()
    
def melhores_tempos():
    """Encontra os melhores tempos para 5k, 10k ou 21k e a sua respetiva data
    """
    print("Não consegui terminar")
    return
    tempo=[]
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
        os.system("cls")
        dist=["5k", "10k", "21k"]
        for x in len(dist):
            verificar=dist[x]
            y=consulta_distancia(verificar)
            #Quebra de racicocínio, não consegui terminar

def progresso_pessoal():
    '''
    Teria de fazer um split na data e fazer a correspondencia dos numeros com o respetivo mês. Teria de remover o k das distâncias e depois usar o sum para  dar os totais. Depois imprimir.
    '''
    with open(file_path, 'w', encoding="utf-8") as ficheiro:
        meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        print("Não consegui terminar")
        return

#-------- INÍCIO DO PROGRAMA --------

menu_opcao="1"
while menu_opcao != "0":
    os.system("cls")
    print("\t MENU")
    print("1 - Consulta por distancia")
    print("2 - Consulta melhores tempos")
    print("3 - Gravar progresso")
    print("0 - Sair")
    print("\n")
    menu_opcao=input("\tOpção: ")
    if menu_opcao == "1":
        #Retorna o caminho absoluto do ficheiro Python atualmente em execução.
        root_dir = os.path.dirname(os.path.abspath(__file__))
        #Altera o diretório atual para o diretório do ficheiro python
        os.chdir(root_dir)
        nome_ficheiro = "atividades.txt"
        file_path= ".\\"+nome_ficheiro
        consulta_distancia()
    elif menu_opcao == "2":
        melhores_tempos()
    elif menu_opcao == "3":
        #Retorna o caminho absoluto do ficheiro Python atualmente em execução.
        root_dir = os.path.dirname(os.path.abspath(__file__))
        #Altera o diretório atual para o diretório do ficheiro python
        os.chdir(root_dir)
        nome_ficheiro = "progresso.txt"
        file_path= ".\\ficheiros\\"+nome_ficheiro
        ficheiro_existe()
        progresso_pessoal()