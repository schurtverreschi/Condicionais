distancia = float(input("Digite a distancia percorrida em km: ").replace(",", "."))

if distancia <= 100:
    print("\nValor do pedágio: R$ 10,00")
elif 100 < distancia < 200:
    print("\nValor do pedágio: R$ 20,00")
else:
    print("\nValor do pedágio: R$ 30,00")
