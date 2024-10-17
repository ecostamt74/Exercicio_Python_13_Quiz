# Ler números enquanto forem crescentes e calcular soma, quantidade e média
soma = 0
quantidade = 0
ultimo_numero = float('-inf')

while True:
    numero = float(input("Digite um número: "))
    if numero < ultimo_numero:
        break
    soma += numero
    quantidade += 1
    ultimo_numero = numero

if quantidade > 0:
    media = soma / quantidade
    print(f"Soma: {soma}, Quantidade: {quantidade}, Média: {media}.")
else:
    print("Nenhum número foi digitado.")