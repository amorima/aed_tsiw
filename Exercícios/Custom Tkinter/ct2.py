import customtkinter as ctk # Importa a biblioteca com designação abreviada

app = ctk.CTk() #Invoca a classe CTK,
app.title("Demo com containers")

# Iniciar o CustomTkinter
ctk.set_appearance_mode("light")  # Modo claro ou escuro

# Dimensões da interface da app
app_width = 400
app_height = 700

# Impedir redimensionamento
""" app.resizable(False, False) # width=False, height=False """

# Definir tamanho mínimo

app.minsize(400, 700)

# Obter as dimensões do meu screen (em pixeis)
screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()
# App centrada no screen, em função das suas dimensões# encontrar
x = (screenWidth/2) - (app_width/2)
y = (screenHeight/2) - (app_height/2)
app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# Aqui terá lugar a restante interface gráfica da app / window

label_pais = ctk.CTkLabel(app, text="País", text_color="blue", font=("Helvetica", 14))
label_pais.place(x=15, y=40)

label_continente = ctk.CTkLabel(app, text="Continente", text_color="blue", font=("Helvetica", 14))
label_continente.place(x=15, y=80)

label_hemisferio = ctk.CTkLabel(app, text="Hemisfério", text_color="blue", font=("Helvetica", 14))
label_hemisferio.place(x=15, y=120)

label_idioma = ctk.CTkLabel(app, text="Idioma Oficial", text_color="blue", font=("Helvetica", 14))
label_idioma.place(x=400, y=40)

#Caixa de texto
str_pais = ctk.StringVar()
str_pais.set("Portugal")
entry_pais = ctk.CTkEntry(app, placeholder_text="Indique um país", textvariable= str_pais, width=150)
entry_pais.place(x=100, y=40)

#ComboBox
lista = ["Africa", "Asia", "América","Europa", "Oceania"]
comb_continente = ctk.CTkComboBox(app, values=lista, width=150, command="")
comb_continente.place(x=100, y= 80)
comb_continente.set("Asia") #Valor por defeito

#Radio Button (Apenas uma opção pode estar selecionada)
radio_variable = ctk.StringVar(value="Norte")
radiobutton1 = ctk.CTkRadioButton(app, text="Norte",variable = radio_variable, value="Norte")
radiobutton1.place(x=100, y=124)

radiobutton2 = ctk.CTkRadioButton(app, text="Sul",variable = radio_variable, value="Sul")
radiobutton2.place(x=100, y=154)

#Check Box - Idiomas
check_var1 = ctk.StringVar(value="off")
check_var2 = ctk.StringVar(value="on")
check_var3 = ctk.StringVar(value="off")
check_var4 = ctk.StringVar(value="off")

checkbox_en = ctk.CTkCheckBox(app, text="Inglês", variable = check_var1, onvalue="on", offvalue="off")
checkbox_pt = ctk.CTkCheckBox(app, text="Português", variable = check_var2, onvalue="on", offvalue="off")
checkbox_fr = ctk.CTkCheckBox(app, text="Francês", variable = check_var3, onvalue="on", offvalue="off")
checkbox_ou = ctk.CTkCheckBox(app, text="Outro", variable = check_var4, onvalue="on", offvalue="off")

checkbox_en.place(x=360, y=80)
checkbox_pt.place(x=460, y=80)
checkbox_fr.place(x=360, y=110)
checkbox_ou.place(x=460, y=110)

#Botões
#Configurações gerais
largura_botao = 100
altura_botao = 40
padding_botao = 5

botao_guardar = ctk.CTkButton(app, text="Guardar", command="", width = largura_botao, height = altura_botao)
botao_guardar.place(relx=1.0, rely=1.0, x=-(largura_botao + padding_botao*2), y=-padding_botao, anchor="se")

botao_limpar = ctk.CTkButton(app, text="Limpar", command="", width = largura_botao, height = altura_botao, state="disabled")
botao_limpar.place(relx=1.0, rely=1.0, x=-(padding_botao), y=-padding_botao, anchor="se")

app.mainloop() # event Listening loop