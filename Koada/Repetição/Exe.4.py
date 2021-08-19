print("*"*30)
print("RENDIMENTO")
print("*"*30)
continuar = "sim"
while continuar == "sim":
    valor = float(input("Qual o valor a ser investido por mês? "))
    txj = float(input("Taxa de juros (Só o n° em %): "))
    txj =(txj/100)+1.00
    for i in range (1, 13):
        if i == 1:
            txj1 = valor*(txj)**i
        if i == 2:
            txj2 = valor*(txj)**i
        if i == 3:
            txj3 = valor*(txj)**i
        if i == 4:
            txj4 = valor*(txj)**i
        if i == 5:
            txj5 = valor*(txj)**i
        if i == 6:
            txj6 = valor*(txj)**i
        if i == 7:
            txj7 = valor*(txj)**i
        if i == 8:
            txj8 = valor*(txj)**i
        if i == 9:
            txj9 = valor*(txj)**i
        if i == 10:
            txj10 = valor*(txj)**i
        if i == 11:
            txj11 = valor*(txj)**i
        if i == 12:
            txj12 = valor*(txj)**i
    txjtotal = txj1+txj2+txj3+txj4+txj5+txj6+txj7+txj8+txj9+txj10+txj11+txj12
    print("O investimento retornado daqui a 1 ano será de ", txjtotal ,"R$")
    continuar = input("Deseja calcular o rendimento para o próximo ano (sim ou não)? ")
print("Até a próxima!")