usuario = input("Digite seu usuário: ")

if usuario == "admin" or usuario == "professor":
    print("Acesso permitido")
else:
    print("Acesso negado")