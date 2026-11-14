# =====================================
# PARTE C - PLACAR E MELHOR DE 3
# =====================================

vitorias_x = 0
vitorias_o = 0
empates = 0
partidas = 0

while vitorias_x < 2 and vitorias_o < 2:

    resultado = input("Digite o resultado (X, O ou E): ")

    while resultado != "X" and resultado != "O" and resultado != "E":
        print("Resultado inválido! Digite X, O ou E.")
        resultado = input("Digite o resultado (X, O ou E): ")

    if resultado == "X":
        vitorias_x = vitorias_x + 1
    elif resultado == "O":
        vitorias_o = vitorias_o + 1
    elif resultado == "E":
        empates = empates + 1

    partidas = partidas + 1

    print("\n======= PLACAR =======")
    print("Vitórias do X:", vitorias_x)
    print("Vitórias do O:", vitorias_o)
    print("Empates:", empates)
    print("Total de partidas:", partidas)
    print("======================")

if vitorias_x == 2:
    print("X é o campeão!")
elif vitorias_o == 2:
    print("O é o campeão!")