import customtkinter as ctk
import os
import CTkMessagebox as CTKmb
from PIL import Image
from tkinter import ttk

# Criar a aplicação (app)
app = ctk.CTk()

# Definir o título da janela
app.title("Exemplo de Interface Gráfica")

# Iniciar o CustomTkinter
ctk.set_appearance_mode("light")  # Modo claro ou escuro (Pode ser "system", "dark" e "light")
ctk.set_default_color_theme("blue")  # Tema padrão (Pode ser "blue", "dark-blue" e "green")

# Dimensões da interface da app
app_width = 600
app_height = 300

# Definir o tamanho da janela usando as variáveis
app.geometry(f"{app_width}x{app_height}")  # Largura x Altura

""" 
# Obter as dimensões do meu screen (em pixeis)
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
# App centrada no screen, em função das suas dimensões# encontrar
x = (screenWidth/2) - (app_width/2)
y = (screenHeight/2) - (app_height/2)
app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
"""

# Definir tamanho mínimo com as variáveis
app.minsize(app_width, app_height)

# Tornar a janela responsiva
app.resizable(True, True)  # Permite redimensionar a janela


# FRAME 2
frameIdiomas = ctk.CTkScrollableFrame(app, width=270, height=200, orientation="vertical",
fg_color="black")

frameIdiomas.place(x=50, y=285)

# Iniciar o loop da interface gráfica
app.mainloop()
