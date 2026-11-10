
# =====================================
# PARTE C - PLACAR ACUMULADO
# =====================================

# Inicialização das variáveis do placar
vitorias_x = 0
vitorias_o = 0
empates = 0

# Recebe o resultado da partida
resultado = input("Digite o resultado (X, O ou E para empate): ").strip().upper()

# Verifica quem venceu ou se houve empate
if resultado == "X":
    vitorias_x = vitorias_x + 1
elif resultado == "O":
    vitorias_o = vitorias_o + 1
elif resultado == "E":
    empates = empates + 1
else:
    print("Resultado inválido!")

# Mostra o placar atualizado
print("\n======= PLACAR =======")
print("Vitórias do X:", vitorias_x)
print("Vitórias do O:", vitorias_o)
print("Empates:", empates)
print("======================")
