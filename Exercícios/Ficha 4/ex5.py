import os

# Limpa a consola
os.system("cls")

def maior_faturacao(faturacao):
    maximo=max(faturacao)
    return maximo

def menor_faturacao(faturacao):
    minimo=min(faturacao)
    return minimo

def media_faturacao(faturacao):
    media=sum(faturacao)/len(faturacao)
    return media

meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

faturacao=[]
while len(faturacao) < 12: #pede que o utilizador introduza 10 números inteiros
    numero_introduzido=int(input((f"Faturação do mês {meses[len(faturacao)]}: ")))
    faturacao.append(numero_introduzido)

print(f"Mês de maior faturação: {meses[faturacao.index(maior_faturacao(faturacao))]}")
print(f"Mês de menor faturação: {meses[faturacao.index(menor_faturacao(faturacao))]}")
print(f"Valor médio de faturação: {media_faturacao(faturacao)}")