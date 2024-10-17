# Ler 2 valores distintos do usuário e escrever o maior deles
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior entre {num1} e {num2} é {num1}.")
else:
    print(f"O maior entre {num1} e {num2} é {num2}.")