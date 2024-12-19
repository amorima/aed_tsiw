def ficheiro_existe():
    """Verifica se o ficheiro existe no filepath, caso não exista cria-o
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="utf-8"):
            pass

#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------

""" String: Se o ficheiro for lido como uma string, podes usar in ou métodos como find() e count(). """

with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
    conteudo = ficheiro.read()
    if "palavra" in conteudo:
        print("Encontrado!")
    else:
        print("Não encontrado.")

#-------------------------------------------------------------------------

""" Lista de Linhas: Se leres o ficheiro como uma lista, podes iterar sobre as linhas e procurar o valor desejado. """

with open("exemplo.txt", "r", encoding="utf-8") as ficheiro:
    linhas = ficheiro.readlines()
    for linha in linhas:
        if "palavra" in linha:
            print("Encontrado na linha:", linha)

#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------

def consulta_paises():
    """ Imprime os dados do ficheiro linha a linha """
    with open(file_path, 'r', encoding="utf-8") as ficheiro:
        file=ficheiro.readlines()
        os.system("cls")
        print(f"Pais{22*" "}Continente")
        print(f"{38*"-"}")
        for line in file:
            print(line.strip())
    input()

#-------------------------------------------------------------------------
#Escreve e lê ficheiro binário

def ficheiro_existe():
    """Verifica se o ficheiro existe no filepath, caso não exista cria-o
    """
    if not os.path.exists(file_path):
        with open(file_path, 'wb'):
            pass

def escreve_texto(texto):
    """Recebe um texto, converte para binário e depois escreve no ficheiro

    Args:
        texto (str): texto input
    """
    ficheiro_existe()
    texto_bin=bytes(texto, encoding="utf-32")
    with open(file_path, 'wb') as ficheiro:
        ficheiro.write(texto_bin)

def ler_texto():
    """Lê o ficheiro binário e imprime-o na consola
    """
    with open(file_path, 'rb') as ficheiro:
        print(str(ficheiro.read(), encoding="utf-32"))

#-------------------------------------------------------------------------
""" Abre um ficheiro.txt """

nome_ficheiro="paises.txt"
file_path= ".\\files\\"+nome_ficheiro

#-------------------------------------------------------------------------
""" Cria um menu """

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