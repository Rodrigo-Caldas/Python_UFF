a = float(input("Insira o peso em kilogramas (kg) da pessoa: "))
b = float(input("Agora digite a altura da pessoa em metros (m): "))
IMC = a/(b**2)
IMC = round(IMC,2)
if IMC < 16:
    print("O seu Índice de Massa Corporal (IMC) é", IMC ,"e é classificado como Magreza de Grau III.")
elif IMC > 16.0 and IMC < 16.9:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Magreza de Grau II.")
elif IMC > 17.0 and IMC < 18.5:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Magreza de Grau I.")
elif IMC > 18.6 and IMC < 24.9:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Adequado.")
elif IMC > 25.0 and IMC < 29.9:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Pré-Obeso.")
elif IMC > 30.0 and IMC < 34.9:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Obesidade Grau I.")
elif IMC > 35.0 and IMC < 39.9:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Obesidade Grau II.")
elif IMC >= 40.0:
    print("O seu Índice de Massa Corporal (IMC) é", IMC, "e é classificado como Obesidade Grau III.")
