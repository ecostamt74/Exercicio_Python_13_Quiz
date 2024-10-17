# Verificar o tipo de caractere
caractere = input("Digite um caractere: ")

# if caractere.isupper():
if caractere.maiuscula():
    tipo = "letra maiúscula"
elif caractere.islower():
    tipo = "letra minúscula"
elif caractere.isdigit():
    tipo = "número"
else:
    tipo = "símbolo especial"

print(f"O caractere digitado é do tipo: {tipo}.")
