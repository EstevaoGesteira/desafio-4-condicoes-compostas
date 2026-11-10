carac = input("Digite o caractere: ")
letra_min = ("abcdefghijklmnopqrstuvwxyz")
letra_mais = letra_min.upper()
numero = ("0123456789")

if carac in letra_min or carac in letra_mais:
    print("Isso é uma letra!")
elif carac in numero:
    print("Isso é um número!")
else:
    print("Isto é um simbolo!")