#P3ORDABC.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENG. REC. HÍDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 22/09/2020
#NOME: RODRIGO ANUNCIAÇÃO CALDAS     MATRÍCULA: 619056124
#P3ORDABC: Manipulação de Valores (A,B,C)

#a) Leia 3 números inteiros diferentes A, B e C;
#b) Reorganize os valores  de forma a que, ao final, A < B < C.

nome = input("Olá! Por favor, digite seu nome: ")
print("Bem-vindo", nome)

A = int(input("Por favor, digite um número inteiro: "))
print("Seu primeiro número é", A)
B = int(input("Insira outro número inteiro: "))
print("Seu segundo número é", B)
C = int(input("Digite mais um número inteiro: "))
print("Seu terceiro e último número é", C)

if A > B:                             #213, 312, 321
    if B > C:                         #321
        aux = A
        A = C
        C = aux
    else:
        if A > C:                     #312
            aux = C
            C = B
            B = aux         #virou 321
            aux = A
            A = C
            C = aux         #virou 123
        else:                         #213
            aux = B
            B = A
            A = aux
else:                                 #123, 132, 231
    if B > C:                         #132, 231
        if A > C:                     #231
            aux = B
            B = C
            C = aux             #virou 213
            aux = B
            B = A
            A = aux             #virou 123
        else:                       #132
            aux = C
            C = B
            B = aux             #virou 123

print("A ordem ficou:",A,"<",B,"<",C)