letra = input("Digite a letra: ")
minus = ("a","e","i","o","u")
mais = ("A","E","I","O","U")

if letra in minus or letra in mais:
    print("Essa letra é uma vogal!")
else:
    print("Essa letra não é uma vogal")
