usuario = input("Digite o seu usuário: ")
senha = input("Digite sua senha: ")
usuarios = ("admin", "user")

if usuario in usuarios and senha == "1234":
    print("Acesso concedido")
else:
    print("Acesso negado")

