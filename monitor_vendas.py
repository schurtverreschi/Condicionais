maca = int(input("Digite a quantidade de maçãs vendidas:"))
banana = int(input("Digite a quantidade de bananas vendidas:"))

if maca > banana:
    print("\nAs maçãs tiveram mais vendas.\n")
elif maca < banana:
    print("\nAs bananas tiveram mais vendas.\n")
else:
    print("\nAs maçãs e bananas venderam o mesmo.\n")
