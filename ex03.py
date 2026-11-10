idade = int(input("Digite a sua idade: "))
documento = input("Você possui documento? (s/n)")

if idade >= 18 and documento == "s":
    print("Entrada permitida!")
else:
    print("Entrada negada!")
