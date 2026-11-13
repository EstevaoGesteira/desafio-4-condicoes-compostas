interesse = input("Interesse (tecnologia/arte/esportes):").lower()
nivel = input("Nível (iniciante/avançado): ").lower()

if interesse in ("tecnologia", "arte") and nivel =="iniciante":
    print("Curso básico")
elif interesse in ("tecnologia", "arte") and nivel =="avançado":
    print("Curso avançado")
else:
    print("Curso geral")