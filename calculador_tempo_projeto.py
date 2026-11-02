atividade_a = int(input("Informe os dias para a atividade A: "))
atividade_b = int(input("Informe os dias para a atividade B: "))
atividade_c = int(input("Informe os dias para a atividade C: "))

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print("\nErro: Os dias não podem ser negativos\n")
else:
    tempo_total = atividade_a + atividade_b + atividade_c
    print(f"\nTempo total para realização do projeto: {tempo_total}\n")
