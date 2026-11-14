# JOGO DA VELHA NO TERMINAL
# Matriz 3x3, for aninhado, while e if (só o conteúdo visto em aula)

# ---------- Parte A (Guilherme): criação da matriz do tabuleiro ----------
tab = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# ---------- Parte C (Mayara): variáveis do placar ----------
vitorias_x = 0
vitorias_o = 0
empates = 0
partidas = 0

opcao = ""
while opcao != "4":
    print("")
    print("===== JOGO DA VELHA =====")
    print("1 - Jogar (melhor de 3)")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Parte C: desafio melhor de 3 (a série acaba quando alguém chega a 2 vitórias)
        serie_x = 0
        serie_o = 0
        while serie_x < 2 and serie_o < 2:

            # Parte C: limpa a matriz (for de fora = linhas, for de dentro = colunas)
            for i in range(3):
                for j in range(3):
                    tab[i][j] = " "

            simbolo = "X"
            venceu = False
            empate = False

            # sequência de jogadas da partida
            while venceu == False and empate == False:

                # Parte A: exibe o tabuleiro
                print("")
                print("   1 2 3")
                for i in range(3):
                    print(i + 1, end="  ")
                    for j in range(3):
                        print(tab[i][j], end=" ")
                    print()
                print("Vez do jogador", simbolo)

                # Parte A: valida a linha escolhida
                linha_valida = False
                while linha_valida == False:
                    entrada = input("Digite a linha (1 a 3): ")
                    for n in range(1, 4):
                        if entrada == str(n):
                            linha = n - 1
                            linha_valida = True
                    if linha_valida == False:
                        print("Linha invalida! Tente novamente.")

                # Parte A: valida a coluna escolhida
                coluna_valida = False
                while coluna_valida == False:
                    entrada = input("Digite a coluna (1 a 3): ")
                    for n in range(1, 4):
                        if entrada == str(n):
                            coluna = n - 1
                            coluna_valida = True
                    if coluna_valida == False:
                        print("Coluna invalida! Tente novamente.")

                # Parte A: verifica casa ocupada e pede outra jogada
                while tab[linha][coluna] != " ":
                    print("Casa ocupada! Escolha outra posicao.")
                    linha_valida = False
                    while linha_valida == False:
                        entrada = input("Digite outra linha (1 a 3): ")
                        for n in range(1, 4):
                            if entrada == str(n):
                                linha = n - 1
                                linha_valida = True
                        if linha_valida == False:
                            print("Linha invalida! Tente novamente.")
                    coluna_valida = False
                    while coluna_valida == False:
                        entrada = input("Digite outra coluna (1 a 3): ")
                        for n in range(1, 4):
                            if entrada == str(n):
                                coluna = n - 1
                                coluna_valida = True
                        if coluna_valida == False:
                            print("Coluna invalida! Tente novamente.")

                # Parte A: marca a jogada
                tab[linha][coluna] = simbolo

                # Parte B: verifica as 3 linhas e as 3 colunas
                for i in range(3):
                    if tab[i][0] == simbolo and tab[i][1] == simbolo and tab[i][2] == simbolo:
                        venceu = True
                    if tab[0][i] == simbolo and tab[1][i] == simbolo and tab[2][i] == simbolo:
                        venceu = True

                # Parte B: verifica as 2 diagonais
                if tab[0][0] == simbolo and tab[1][1] == simbolo and tab[2][2] == simbolo:
                    venceu = True
                if tab[0][2] == simbolo and tab[1][1] == simbolo and tab[2][0] == simbolo:
                    venceu = True

                # Parte B: conta as casas vazias com for aninhado
                vazias = 0
                for i in range(3):
                    for j in range(3):
                        if tab[i][j] == " ":
                            vazias = vazias + 1
                if vazias == 0 and venceu == False:
                    empate = True

                # passa a vez (só se a partida continua)
                if venceu == False and empate == False:
                    if simbolo == "X":
                        simbolo = "O"
                    else:
                        simbolo = "X"

            # mostra o tabuleiro final
            print("")
            print("   1 2 3")
            for i in range(3):
                print(i + 1, end="  ")
                for j in range(3):
                    print(tab[i][j], end=" ")
                print()

            # Parte B: mensagem de resultado da partida
            if venceu == True:
                print("O jogador", simbolo, "venceu!")
            else:
                print("Deu empate!")

            # Parte C: atualiza o placar no fim da partida
            partidas = partidas + 1
            if venceu == True and simbolo == "X":
                vitorias_x = vitorias_x + 1
                serie_x = serie_x + 1
            elif venceu == True and simbolo == "O":
                vitorias_o = vitorias_o + 1
                serie_o = serie_o + 1
            else:
                empates = empates + 1
            print("PLACAR: X =", vitorias_x, "| O =", vitorias_o, "| Empates =", empates)

        if serie_x == 2:
            print("X é o campeão da série!")
        else:
            print("O é o campeão da série!")

    elif opcao == "2":
        print("")
        print("REGRAS DO JOGO DA VELHA")
        print("Dois jogadores se alternam marcando X ou O em uma casa vazia.")
        print("Vence quem completar uma linha, coluna ou diagonal.")
        print("Se o tabuleiro encher sem vencedor, é empate.")
        print("No modo melhor de 3, vence a série quem chegar a 2 vitórias.")

    elif opcao == "3":
        print("")
        print("PLACAR GERAL")
        print("Partidas:", partidas)
        print("Vitórias de X:", vitorias_x)
        print("Vitórias de O:", vitorias_o)
        print("Empates:", empates)
        if partidas > 0:
            porc_x = vitorias_x * 100 / partidas
            porc_o = vitorias_o * 100 / partidas
            print("X venceu", int(porc_x * 10) / 10, "% das partidas")
            print("O venceu", int(porc_o * 10) / 10, "% das partidas")

    elif opcao == "4":
        print("Até a próxima!")

    else:
        print("Opção inválida! Digite um número de 1 a 4.")