# Ler 3 números quaisquer do usuário e escrever a maior diferença entre 2 deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
diferenca = maior - menor

print(f"A maior diferença entre os números lidos é {diferenca}.")