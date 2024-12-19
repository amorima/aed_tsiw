'''Implemente um pequeno programa quem em função da introdução da idade do
utilizador, determine a respetiva Etapa da Vida, de acordo com a imagem
abaixo.
O resultado pretendido pelo seu programa é imprimir o que se encontra a
negrito na imagem abaixo.
Por exemplo:
• Para alguém com 20 anos o resultado esperado deve ser Adultez – Jovem
Adulto.
• Para alguém com 40 anos o resultado esperado deve ser Adultez – maia
idade.'''

print("ETAPA DA VIDA") #Título
print("\n")
idade=int(input("Introduza a dua idade: ")) #input de idade
print("\n")


#Seletor da Etapa da Vida
if idade <3:
    print("Primeira Infância")
elif 3<= idade <7:
    print("Infância Intermediária")
elif 7<= idade <13:
    print("Pré-adolescência ")
elif 10<= idade <15:
    print("Adolescência - Puberdade")
elif 15<= idade <20:
    print("Adolescência Tardia")
elif 20<= idade <40:
    print("Adultez - Jovem Adulto")
elif 40<= idade <60:
    print("Adultez - Meia-idade")
elif 60<= idade <75:
    print("Terceira Idade - Idoso Jovem ")
elif idade >75:
    print("Terceira Idade - Idoso Velho")