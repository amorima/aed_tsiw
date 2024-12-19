import os
from colorama import Fore, Style
import random

def limpar_ecra():
    """Limpa o ecrã em vários sistemas operativos"""
    os.system("cls" if os.name == "nt" else "clear")

def jogada(tabuleiro, jogador):
    """Faz a jogada do jogador (utilizador ou computador).

    Args:
        tabuleiro (list): O tabuleiro do jogo.
        jogador (str): O jogador atual ("O" ou "X").

    Returns:
        tuple: Coordenadas (linha, coluna) da jogada.
    """
    if jogador == "O":
        # Jogador
        while True:
            try:
                linha = int(input("Linha (1-6): ")) - 1
                coluna = int(input("Coluna (1-7): ")) - 1
                if 0 <= linha < 6 and 0 <= coluna < 7 and tabuleiro[linha][coluna] == "*":
                    return linha, coluna
                else:
                    print("Posição inválida! Escolha outra.")
            except ValueError:
                print("Entrada inválida! Introduza números para linha e coluna.")
    else:
        # Jogador computador
        for prioridade in [3, 2]:
            # Prioridade: tentar ganhar ou bloquear o jogador humano
            for linha in range(6):
                for coluna in range(7):
                    if tabuleiro[linha][coluna] == "*":
                        # Simula a jogada para o computador
                        tabuleiro[linha][coluna] = "X"
                        if verificar_vitoria(tabuleiro, linha, coluna, "X"):
                            tabuleiro[linha][coluna] = "*"  # Reverte a simulação
                            return linha, coluna

                        # Simula a jogada para o jogador humano
                        tabuleiro[linha][coluna] = "O"
                        if verificar_vitoria(tabuleiro, linha, coluna, "O"):
                            tabuleiro[linha][coluna] = "*"  # Reverte a simulação
                            return linha, coluna

                        tabuleiro[linha][coluna] = "*"  # Reverte a simulação

        # Escolhe uma posição aleatória caso nenhuma jogada prioritária seja encontrada
        while True:
            linha = random.randint(0, 5)
            coluna = random.randint(0, 6)
            if tabuleiro[linha][coluna] == "*":
                return linha, coluna

def imprimir(tabuleiro):
    """Imprime o tabuleiro com cores aplicadas."""
    for linha in tabuleiro:
        linha_colorida = []
        for celula in linha:
            if celula == "O":
                linha_colorida.append(Fore.CYAN + "O" + Style.RESET_ALL)
            elif celula == "X":
                linha_colorida.append(Fore.YELLOW + "X" + Style.RESET_ALL)
            else:
                linha_colorida.append(celula)
        print(" ".join(linha_colorida))

def verificar_vitoria(tabuleiro, linha, coluna, jogador):
    """Verifica se há 4 peças consecutivas do jogador a partir da posição (linha, coluna)."""
    direcoes = [
        (0, 1),   # Horizontal direita
        (1, 0),   # Vertical para baixo
        (1, 1),   # Diagonal principal (\u2198)
        (1, -1)   # Diagonal secundária (\u2199)
    ]

    for d_linha, d_coluna in direcoes:
        contagem = 1
        i, j = linha + d_linha, coluna + d_coluna
        while 0 <= i < 6 and 0 <= j < 7 and tabuleiro[i][j] == jogador:
            contagem += 1
            i += d_linha
            j += d_coluna

        i, j = linha - d_linha, coluna - d_coluna
        while 0 <= i < 6 and 0 <= j < 7 and tabuleiro[i][j] == jogador:
            contagem += 1
            i -= d_linha
            j -= d_coluna

        if contagem >= 4:
            return True

    return False

# Inicio do tabuleiro e variáveis
quatro = [["*" for _ in range(7)] for _ in range(6)]
vez = "O"  # Jogador 1 começa
jogo = "em curso"

while jogo == "em curso":
    limpar_ecra()
    print(Fore.BLUE + Style.BRIGHT + "QUATRO EM LINHA\n" + Style.RESET_ALL)
    print(f"Vez do jogador {'1 (O)' if vez == 'O' else '2 (X)'}\n")
    imprimir(quatro)
    print("\n")

    linha, coluna = jogada(quatro, vez)

    # Atualizar o tabuleiro
    quatro[linha][coluna] = vez

    # Verificar se o jogador atual ganhou
    if verificar_vitoria(quatro, linha, coluna, vez):
        limpar_ecra()
        imprimir(quatro)
        print(Fore.GREEN + f"\nO {'jogador (O)' if vez == 'O' else 'computador (X)'} ganhou o jogo!" + Style.RESET_ALL)
        jogo = "terminado"
        break

    # Alternar a vez
    vez = "X" if vez == "O" else "O"