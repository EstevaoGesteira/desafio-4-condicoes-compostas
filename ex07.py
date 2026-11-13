placa = input("Placa (ex.: ABC1234): ").upper()
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

if (len(placa) == 7
        and placa[0] in letras and placa[1] in letras and
placa[2] in letras
        and placa[3] in numeros and placa[4] in numeros
        and placa[5] in numeros and placa[6] in numeros):
    print("Placa válida")
else:
    print("Placa inválida")