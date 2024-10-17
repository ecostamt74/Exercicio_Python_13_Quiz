# Função para realizar as operações
def calcular(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtração':
        return num1 - num2
    elif operacao == 'multiplicação':
        return num1 * num2
    elif operacao == 'divisão':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operação inválida!"

# Solicita ao usuário os números e a operação
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (soma, subtração, multiplicação, divisão): ").strip().lower()

    resultado = calcular(operacao, numero1, numero2)
    print(f"O resultado da {operacao} é: {resultado}")

except ValueError:
    print("Por favor, digite números válidos.")
