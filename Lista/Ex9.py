# Encontrar o maior entre n números fornecidos
n = int(input("Digite a quantidade de números a ser lida: "))

maior = float('-inf')
for _ in range(n):
    numero = float(input("Digite um número: "))
    if numero > maior:
        maior = numero

print(f"O maior número digitado foi {maior}.")