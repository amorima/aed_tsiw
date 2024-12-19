import random
import os #operating system
continuar="S"

while continuar.upper() == "S":
    os.system("cls")
    numeroAleatorio=random.randint(1, 50)
    palpite=int(input("Indique o seu palpite: "))
    tentativas=10
    quantidadeTentativas=1
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
        tentativas=10
        quantidadeTentativas=0
        continuar=input("Novo Jogo(S/N)?: ")
        if continuar == "S":
            palpite=int(input("Indique o seu palpite: "))
            continue
    print("ACERTOU")
    print(f"Parabéns! Acertou em {quantidadeTentativas} tentativas")
    tentativas=10
    quantidadeTentativas=0
    continuar=input("Novo Jogo(S/N)?: ")
    if continuar == "S":
        palpite=int(input("Indique o seu palpite: "))
        continue
    else:
        exit()