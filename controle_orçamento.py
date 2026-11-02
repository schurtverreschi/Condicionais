ORCAMENTO = 3000
gastos_mes = float(input("Informe o total de despesas do mês (R$): "))

if gastos_mes >= ORCAMENTO:
    print("Atenção! Você ultrapassou o limite de gastos do mês.")
else:
    print("Você está dentro do limite de gastos do mês.")
