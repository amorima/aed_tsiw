""" 
O jogador 1 usa as "peças" O
O jogador 2 usa as "peças" X 
"""

import os
from colorama import Fore

def limpar_ecra():
    """Limpa o ecrã em vários sistemas operativos
    """
    os.system("cls" if os.name == "nt" else "clear")

def jogada():
    """Pede para fazer a jogada introduzindo a linha e a coluna. Retorna as posições introduzidas.

    Returns:
        int: Podição na matriz do jogo
    """
    while True:
        try:
            linha = int(input("linha (1-6): ")) - 1
            coluna = int(input("Coluna (1-7): ")) - 1
            if 0 <= linha < 6 and 0 <= coluna < 7:
                return linha, coluna
            else:
                print("Posição inválida! As linhas vão de 1 a 6 e as colunas de 1 a 7.")
        except ValueError:
            print("Entrada inválida! Introduz números para linha e coluna.")

def imprimir(tabuleiro):
    """imprime o tabuleiro

    Args:
        tabuleiro (list): imprime a matriz do jogo
    """
    for linha in tabuleiro:
        print(" ".join(linha))

def verificar_vitoria(tabuleiro, linha, coluna, jogador):
    """Verifica se há 4 peças consecutivas do jogador a partir da posição (linha, coluna, diagonal).
    """
    # Direções: (d_linha, d_coluna)
    direcoes = [
        (0, 1),   # Horizontal direita
        (1, 0),   # Vertical para baixo
        (1, 1),   # Diagonal principal (↘)
        (1, -1)   # Diagonal secundária (↙)
    ]

    for d_linha, d_coluna in direcoes:
        contagem = 1  # Conta a peça atual

        # Verificar na direção positiva
        i, j = linha + d_linha, coluna + d_coluna
        while 0 <= i < 6 and 0 <= j < 7 and tabuleiro[i][j] == jogador:
            contagem += 1
            i += d_linha
            j += d_coluna

        # Verificar na direção negativa
        i, j = linha - d_linha, coluna - d_coluna
        while 0 <= i < 6 and 0 <= j < 7 and tabuleiro[i][j] == jogador:
            contagem += 1
            i -= d_linha
            j -= d_coluna

        # Verificar se encontrou 4 em linha
        if contagem >= 4:
            return True

    return False

# Inicio do tabuleiro e variáveis
quatro = [["*" for _ in range(7)] for _ in range(6)]
vez = "O"  # Jogador 1 começa
jogo = "em curso"

while jogo == "em curso":
    limpar_ecra()
    print(f"Vez do jogador {'1 (O)' if vez == 'O' else '2 (X)'}\n")
    imprimir(quatro)
    print("\n")

    linhas, coluna = jogada()

    # Verificar se a posição está ocupada
    if quatro[linhas][coluna] != "*":
        print("Posição indisponível, por favor selecione outra.")
        input("Pressiona Enter para tentar novamente...")
        continue

    # Atualizar o tabuleiro
    quatro[linhas][coluna] = vez

        # Verificar se o jogador atual ganhou
    if verificar_vitoria(quatro, linhas, coluna, vez):
        limpar_ecra()
        imprimir(quatro)
        print(f"\nJogador {'1 (O)' if vez == 'O' else '2 (X)'} ganhou o jogo!")
        jogo = "terminado"
        break

    # Alternar a vez
    vez = "X" if vez == "O" else "O"