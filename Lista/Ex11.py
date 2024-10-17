# Verificar se um algarismo aparece em um número
numero = input("Digite um número inteiro: ")
algarismo = input("Digite um algarismo (0-9): ")

if algarismo in numero:
    print(f"O algarismo {algarismo} aparece no número {numero}.")
else:
    print(f"O algarismo {algarismo} não aparece no número {numero}.")
