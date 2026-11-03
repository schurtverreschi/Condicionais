renda = float(input("Informe sua renda mensal: "))
parcela = float(input("Informe o valor da parcela desejada: "))

if renda < 2000:
    print("\nEmpréstimo negado: Renda mensal inferior a R$ 2000,00.")
elif parcela > (renda * 0.3):
    print("\nEmpréstimo negado: valor da parcela superior a 30% da renda mensal.")
else:
    print("Empréstimo aprovado.")
