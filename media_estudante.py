nota_um = float(input("Insira primeira nota: ").replace(",", "."))
nota_dois = float(input("Insira segunda nota: ").replace(",", "."))
nota_tres = float(input("Insira terceira nota: ").replace(",", "."))
media = (nota_um + nota_dois + nota_tres) / 3

print(f"\nMédia: {media:.2f}")

if media >= 7:
    print("\nAprovado\n")
elif 5 <= media < 7:
    print("\nRecuperação\n")
else:
    print("\nReprovado\n")
