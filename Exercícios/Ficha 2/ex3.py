'''
Jogo Adivinha o número! Elabore um programa que simule o jogo da adivinha de um número. O programa deve começar por gerar um número aleatório (entre 1 e 50), permitindo que o jogador tente, iterativamente, adivinhar o número gerado pelo computador. 
'''
import random

numeroAleatorio=random.randint(1, 50)
palpite=int(input("Indique o seu palpite: "))
tentativas=10
quantidadeTentativas=0

while numeroAleatorio != palpite:
    if palpite > numeroAleatorio:
        print("O seu número é MAIOR")
    else:
        print("O seu número é MENOR")
    palpite=int(input("Indique o seu palpite: "))
    tentativas-=1
    quantidadeTentativas+=1
    if tentativas > 1:
        continue
    print("Esgotou as 10 tentativas :(")
    exit()

print("ACERTOU")
print(f"Parabéns! Acertou em {quantidadeTentativas} tentativas")