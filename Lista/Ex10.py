# Calcular anos necessários para a população do país A ultrapassar a do país B
populacao_A = 90000000
populacao_B = 200000000
taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015
anos = 0

while populacao_A < populacao_B:
    populacao_A *= (1 + taxa_crescimento_A)
    populacao_B *= (1 + taxa_crescimento_B)
    anos += 1

print(f"Serão necessários {anos} anos para a população do país A ultrapassar a do país B.")
