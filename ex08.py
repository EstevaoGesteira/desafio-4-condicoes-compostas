cargo = input("Cargo (admin/editor/visitante): ")
acao = input("Ação (ler/editar/excluir): ")

if cargo == "admin" and acao in ("ler", "editar","excluir"):
    print("Permitido")
elif cargo == "editor" and acao in ("ler", "editar"):
    print("Permitido")
elif cargo == "visitante" and acao == "ler":
    print("Permitido")
else:
    print("Negado")