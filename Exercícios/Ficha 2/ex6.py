'''
Elabore um programa que ilustre os primeiros n termos da sequência de
Fibonacci, sendo que o número de termos desejados (n) deve ser indicado
pelo utilizador.
Na sequência de Fibonacci, cada termo resulta da soma dos dois anteriores.
'''

ultimo_numero = 0
numero_atual = 1
contador = 0
n_termos=int(input("Nº de termos a imprimir: "))
sequencia=(f"Primeiros {n_termos} termos da sequência de Fibonacci: ")

# Verificar se o número de termos é válido
if n_termos <= 0:
    print("Por favor, insira um número positivo.")
elif n_termos == 1:
    print(ultimo_numero)
else:
    # Imprime os primeiros n termos da sequência de Fibonacci
    while contador < n_termos:
        sequencia += str(ultimo_numero)
        if contador < n_termos - 1:
            sequencia += ", "
        proximo_numero = ultimo_numero + numero_atual
        ultimo_numero = numero_atual
        numero_atual = proximo_numero
        contador += 1

print(sequencia)
