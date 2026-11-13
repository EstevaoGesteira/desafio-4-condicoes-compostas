senha = input("Crie uma senha: ")

tem_numero = ("0" in senha or "1" in senha or "2" in senha
or "3" in senha

or "4" in senha or "5" in senha or "6" in

senha

or "7" in senha or "8" in senha or "9" in

senha)
if tem_numero and len(senha) >= 6:
    print("Senha válida")
else:
    print("Senha inválida")