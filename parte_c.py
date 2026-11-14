# =====================================
# PARTE C - VARIAVEIS DO PLACAR
# =====================================

vitorias_x = 0
vitorias_o = 0
empates = 0
partidas = 0

resultado = input("Digite o resultado (X, O ou E): ")
while resultado != "X" and resultado != "O" and resultado != "E":
    print("Resultado inválido! Digite X, O ou E.")
    resultado = input("Digite o resultado (X, O ou E): ")
if resultado == "X":
    vitorias_x = vitorias_x + 1
    partidas = partidas + 1
elif resultado == "O":
    vitorias_o = vitorias_o + 1
    partidas = partidas + 1
elif resultado == "E":
    empates = empates + 1
    partidas = partidas + 1
print("\n======= PLACAR =======")
print("Vitórias do X:", vitorias_x)
print("Vitórias do O:", vitorias_o)
print("Empates:", empates)
print("Total de partidas:", partidas)
print("======================")