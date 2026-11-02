peso = int(input("Informe seu peso(kg): "))
altura = float(input("Informe sua altura(m):"))
imc = peso / (altura**2)

print(f"\nSeu IMC é {imc:.2f}")

if imc >= 25:
    print("\nVocê está acima do peso.\n")
elif imc >= 18.5:
    print("\nVocê está dentro da faixa de peso ideal.\n")
else:
    print("\nVocê está abaixo do peso.\n")
