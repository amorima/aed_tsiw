
# Número: 40240119
# Nome: António Manuel Cruz Barreto Amorim

# Biblioteca Tkinter: UI
import customtkinter
import CTkMessagebox
from PIL import Image

from tkinter import ttk          # treeview
import os


#----------------FUNÇÕES E CÓDIGO DE APOIO -----------------------------
#-----------------------------------------------------------------------

#Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
#Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)


file_path_meses = os.path.join("files", "meses.txt")
file_path_Dezembro = os.path.join("files", "Dezembro.txt")
file_path_Novembro = os.path.join("files", "Novembro.txt")
file_path_Outubro = os.path.join("files", "Outubro.txt")

#----------------Message Boxes -----------------------------------------
#-----------------------------------------------------------------------
def consultar_mes():
    """
    Verifica se está algum mês selecionado na combobox, caso não esteja dá erro!
    Deveria ter mais um elif para verificar se o mês tem ou não valores.
    """
    # Verificar se algum mês foi selecionado
    if combobox_mes.get() == "":
        CTkMessagebox.CTkMessagebox(app, title="Erro", message="Não selecionou um mês!", icon="warning")


  
# ---------------INICIO DA INTERFACE GRAFICA  ---------------------
#-----------------------------------------------------------------
def renderWindow(appWidth, appHeight, appTitle):
    """
    Renderiza a window da app, com as dimensões e título dos argumentos
    """
    app.title(appTitle)
    # Obter as dimensões do meu screen (em pixeis)
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    # App centrada no screen, em função das suas dimensões# encontrar o 
    x = (screenWidth/2) - (appWidth/2)
    y= (screenHeight/2) - (appHeight/2)
    app.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    app.resizable(False, False) 




app = customtkinter.CTk()
renderWindow(450, 550, "DespesasApp")

#--- FRAME 1 - frame com os critérios de consulta ------------------------
frame1 = customtkinter.CTkFrame(app, width=430, height=170, fg_color="gray")
frame1.place(x=10, y=10)

labelMes = customtkinter.CTkLabel(frame1, text = "Mês de Consulta de Despesas: ")
labelMes.place(x=20, y= 10)


# Inicialização da lista antes do loop
lista = []

# Abrir o ficheiro 'meses.txt' e carregar os meses na lista
with open(file_path_meses, 'r') as file:
    for linha in file:
        lista.append(linha.strip())  # Adiciona cada linha à lista, removendo espaços extras

mes = customtkinter.StringVar()
# Combobox que deverá conter os meses de Janeiro a Dezembro, a partir da leitura do ficheiro meses.txt

combobox_mes = customtkinter.CTkComboBox(
    frame1, 
    height=12, 
    variable=mes, 
    values=lista  # Passa a lista de meses para o ComboBox
)
combobox_mes.place(x=250, y=10)


rbState = customtkinter.StringVar()
#------Ativar, por defeito, o radioButton com a opção Todas

rb1 = customtkinter.CTkRadioButton(frame1, text = "Dinheiro",   variable = rbState, value = "Dinheiro")
rb2 = customtkinter.CTkRadioButton(frame1, text = "Credito",    variable = rbState, value = "Credito")
rb3 = customtkinter.CTkRadioButton(frame1, text = "Todas",      variable = rbState, value = "Todas")
rb1.place (x=20, y=60)
rb2.place (x=20, y=90)
rb3.place (x=20, y=120)

button_image = customtkinter.CTkImage(light_image=Image.open(".\\images\\lupa.png"),
                            dark_image=Image.open(".\\images\\lupa.png"),
                            size=(64, 64))  # Define o tamanho da imagem

btnConsultar = customtkinter.CTkButton(frame1, width=150, height=70, text = "Consultar", text_color="cyan", image=button_image, compound="right",
                                        command=consultar_mes)

btnConsultar.place(x=235, y=70)

#----------------FRAME COM A TREEVIEW ----------------------------------
#-----------------------------------------------------------------------
frame2 = customtkinter.CTkFrame(app, width=430, height=320)
frame2.place(x=10, y=200)

tree = ttk.Treeview(frame2, columns = ("Descrição", "Valor", "Estado"), show = "headings", height = 17)
tree.column("Descrição", width = 240, anchor = "w")
tree.column("Valor", width = 130, anchor = "c")
tree.column("Estado", width = 130, anchor = "c")
tree.heading("Descrição", text = "Descrição")
tree.heading("Valor", text = "Valor")
tree.heading("Estado", text = "Estado")
tree.place(x=17, y=15)


#----------------Nº de Despesas e Valor, na base da janela da app
#------------------------------------------------------------------
lblDespesas = customtkinter.CTkLabel(app, text = "Nº de Despesas:" )
lblTotal = customtkinter.CTkLabel(app, text = "Valor Total: ")
lblDespesas.place (x= 50, y=520)
lblTotal.place (x= 250, y=520)

#----- LABEL do Número de Despesas
lblNumDespesas =customtkinter.CTkLabel(app, text = "")
lblNumDespesas.place(x=150, y=520)

# - LABEL do Valor Total de Despesas
lblValorTotal =customtkinter.CTkLabel(app, text = "" )
lblValorTotal.place(x=350, y=520)



app.mainloop()   # event listening loop by calling the mainloop()