import customtkinter as ctk
import os
import CTkMessagebox as CTKmb
from PIL import Image

#-------------------------------------------------
#-------FUNÇÕES DA APP----------------------------
#-------------------------------------------------

# Função para sair da app
def message_ask():
    msg = CTKmb.CTkMessagebox(app, width=300, height=200, title="Sair?",
                        message= "Deseja encerrar a aplicação?",
                        icon="question",
                        option_1="Cancelar",
                        option_2="Não",
                        option_3="Sim"
                        )
    response = msg.get()

    if response == "Sim":
        app.destroy()
    else:
        print("Selecione 'Sim' para sair!")

def presencas():
    frame_presencas = ctk.CTkFrame(app, width=745, height=490, fg_color="#d4d4d4")
    frame_presencas.place(x=250, y=5)
    
    # Criação do botão
    button_pres = ctk.CTkButton(
        master=frame_presencas,                   # Janela ou frame onde o botão será inserido
        text="Ler Ficheiro de Presenças",           # Texto do botão
        text_color="white",           # Cor do texto
        font=("Poppins", 14),         # Fonte e tamanho do texto
        width=320, height=70,         # Tamanho do botão
        fg_color="#3498db",           # Cor de fundo
        hover_color="#2980b9",        # Cor ao passar o rato
        compound="top",              # Posiciona a imagem à esquerda do texto
        corner_radius=10,             # Arredondamento dos cantos
        command=""    # Função a executar ao clicar
    )
    # Posiciona o botão no frame_menu
    button_pres.place(relx=1.0, rely=1.0, x=-5, y=-50, anchor="se")

def consulta():
    frame_consulta = ctk.CTkFrame(app, width=745, height=490, fg_color="#d4d4d4")
    frame_consulta.place(x=250, y=5)

#-------------------------------------------------
#-------GUI---------------------------------------
#-------------------------------------------------

# Criar a aplicação (app)
app = ctk.CTk()

# Definir o título da janela
app.title("Gestão de Presenças")

# Iniciar o CustomTkinter
ctk.set_appearance_mode("light")  # Modo claro ou escuro (Pode ser "system", "dark" e "light")

# Dimensões da interface da app
app_width = 1000
app_height = 500

# Definir o tamanho da janela usando as variáveis
app.geometry(f"{app_width}x{app_height}")  # Largura x Altura

# Definir tamanho mínimo com as variáveis
app.minsize(app_width, app_height)

# Prevenir o redimensionamento da janela
app.resizable(False, False)  # Impede o redimensionamento nas direções horizontal e vertical

# Obter as dimensões do meu screen (em pixeis)
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
# App centrada no screen, em função das suas dimensões
x = (screenWidth/2) - (app_width/2)
y = (screenHeight/2) - (app_height/2)
app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#-------------------------------------------------
#-------INÍCIO DA APLICAÇÃO-----------------------
#-------------------------------------------------

# Retorna o caminho absoluto do ficheiro Python atualmente em execução.
root_dir = os.path.dirname(os.path.abspath(__file__))
# Altera o diretório atual para o diretório do ficheiro python
os.chdir(root_dir)

# Criar um frame container para o menu
frame_menu = ctk.CTkFrame(app, width=240, height=490, fg_color="#d4d4d4")
frame_menu.place(x=5, y=5)

# Criar um frame container para o conteúdo
frame_conteudo = ctk.CTkFrame(app, width=745, height=490, fg_color="#d4d4d4")
frame_conteudo.place(x=250, y=5)

# A imagem deve ser redimensionada para evitar distorções
button_image = ctk.CTkImage(light_image=Image.open(".\\images\\icoOp1.png"),
                            dark_image=Image.open(".\\images\\icoOp1.png"),
                            size=(64, 64))  # Define o tamanho da imagem
# Criação do botão
button = ctk.CTkButton(
    master=frame_menu,                   # Janela ou frame onde o botão será inserido
    text="Gerir Presenças",           # Texto do botão
    text_color="white",           # Cor do texto
    font=("Poppins", 14),         # Fonte e tamanho do texto
    width=230, height=120,         # Tamanho do botão
    fg_color="#3498db",           # Cor de fundo
    hover_color="#2980b9",        # Cor ao passar o rato
    image=button_image,           # Imagem adicionada ao botão
    compound="top",              # Posiciona a imagem à esquerda do texto
    corner_radius=10,             # Arredondamento dos cantos
    command=presencas    # Função a executar ao clicar
)
# Posiciona o botão no frame_menu
button.place(x=5, y=50)

# A imagem deve ser redimensionada para evitar distorções
button2_image = ctk.CTkImage(light_image=Image.open(".\\images\\icoOp2.png"),
                            dark_image=Image.open(".\\images\\icoOp2.png"),
                            size=(64, 64))  # Define o tamanho da imagem
# Criação do botão
button2 = ctk.CTkButton(
    master=frame_menu,                   # Janela ou frame onde o botão será inserido
    text="Consultar Presenças",           # Texto do botão
    text_color="white",           # Cor do texto
    font=("Poppins", 14),         # Fonte e tamanho do texto
    width=230, height=120,         # Tamanho do botão
    fg_color="#3498db",           # Cor de fundo
    hover_color="#2980b9",        # Cor ao passar o rato
    image=button2_image,           # Imagem adicionada ao botão
    compound="top",              # Posiciona a imagem à esquerda do texto
    corner_radius=10,             # Arredondamento dos cantos
    command=consulta    # Função a executar ao clicar
)
# Posiciona o botão no frame_menu
button2.place(x=5, y=190)

# A imagem deve ser redimensionada para evitar distorções
button3_image = ctk.CTkImage(light_image=Image.open(".\\images\\icoOp4.png"),
                            dark_image=Image.open(".\\images\\icoOp4.png"),
                            size=(64, 64))  # Define o tamanho da imagem
# Criação do botão
button3 = ctk.CTkButton(
    master=frame_menu,                   # Janela ou frame onde o botão será inserido
    text="Sair da App",           # Texto do botão
    text_color="white",           # Cor do texto
    font=("Poppins", 14),         # Fonte e tamanho do texto
    width=230, height=120,         # Tamanho do botão
    fg_color="#3498db",           # Cor de fundo
    hover_color="#2980b9",        # Cor ao passar o rato
    image=button3_image,           # Imagem adicionada ao botão
    compound="top",              # Posiciona a imagem à esquerda do texto
    corner_radius=10,             # Arredondamento dos cantos
    command=message_ask      # Função a executar ao clicar
)
# Posiciona o botão no frame_menu
button3.place(x=5, y=330)

# Carregar a imagem (ajustar o caminho para o ficheiro da sua imagem)
image_path = ".\\images\\presencas.png"
imagem = ctk.CTkImage(dark_image=Image.open(image_path), size=(750, 500))  # Define o tamanho (opcional)

# Exibir a imagem num CTkLabel
label_imagem = ctk.CTkLabel(frame_conteudo, text="", image=imagem)
label_imagem.place(relwidth=1, relheight=1)


# Iniciar o loop da interface gráfica
app.mainloop()
