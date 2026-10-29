def mostrar_tabuleiro(tabuleiro):
    print("\n    1   2   3")
    for i, linha in enumerate(tabuleiro):
        print(f"{i + 1}   " + " | ".join(linha))
        if i < 2:
            print("   ---+---+---")


def verificar_vitoria(tabuleiro, jogador):
    # Verifica as linhas
    for linha in tabuleiro:
        if all(celula == jogador for celula in linha):
            return True

    # Verifica as colunas
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    # Verifica a diagonal principal
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True

    # Verifica a diagonal secundária (corrigido para 2 - i)
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"
jogadas = 0

print("JOGO DA VELHA!")

while jogadas < 9:
    mostrar_tabuleiro(tabuleiro)
    print(f"Vez do jogador: {jogador}")

    try:
        linha = int(input("Linha (1 a 3): ")) - 1
        coluna = int(input("Coluna (1 a 3): ")) - 1
    except ValueError:
        print("Digite apenas números!")
        continue

    if not (0 <= linha < 3 and 0 <= coluna < 3):
        print("Posição inválida! Escolha entre 1 e 3.")
        continue

    if tabuleiro[linha][coluna] != " ":
        print("Posição ocupada! Tente novamente.")
        continue

    tabuleiro[linha][coluna] = jogador
    jogadas += 1

    if verificar_vitoria(tabuleiro, jogador):
        mostrar_tabuleiro(tabuleiro)
        print(f"Parabéns! O jogador {jogador} venceu!")
        break

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

else:
    mostrar_tabuleiro(tabuleiro)
    print("Empate! Não há mais posições disponíveis.")
