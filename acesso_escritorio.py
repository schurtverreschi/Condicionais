horario = int(input("Informe o horário atual(24h): "))

if 8 <= horario < 18:
    print("\nEntrada liberada.\n")
else:
    print("Acesso negado: Fora do horário de expediente.")
