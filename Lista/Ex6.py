# Ler 3 valores distintos do usuário e escrever o maior deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
print(f"O maior de 3 valores distintos lidos foi {maior}.")