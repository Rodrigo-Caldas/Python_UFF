#P6REDABC.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENG. REC. HÍDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 29/09/2020
#NOME: RODRIGO ANUNCIAÇÃO CALDAS     MATRÍCULA: 619056124
#P4REDABC: Manipulação de Valores (A,B,C)

#a) Leia 3 números inteiros diferentes (e A sendo diferente de 0) A, B e C;
#b) Reorganize os valores  de forma a que, ao final, A < B < C.
cont = 1
nome = input("Olá! Por favor, digite seu nome: ")
print("Bem-vindo", nome)
print(" ")

A = int(input("Por favor, digite um número inteiro (0 para parar): "))
print("Seu primeiro número é", A)
while A != 0:
    B = int(input("Insira outro número inteiro: "))
    print("Seu segundo número é", B)
    C = int(input("Digite mais um número inteiro: "))
    print("Seu terceiro e último número é", C)

    if A > B:  # 213, 312, 321
        var = A
        A = B
        B = var  # Fica 123, 132, 231
    if B > C:  # 132, 231
        var = B
        B = C
        C = var  # Fica 123, 213
    if A > B:  # 213
        var = A
        A = B
        B = var  # 123
    print(" ")
    print("A ordem ficou:", A, "<", B, "<", C)
    print(" ")
    A = int(input("Por favor, digite um número inteiro (0 para parar): "))
    print("Seu primeiro número é", A)
print("-----------------------------------")
print("Obrigado por utilizar o programa :)")