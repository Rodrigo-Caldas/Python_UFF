#P2LEIMP.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENG. REC. HÍDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 15/09/2020
#NOME: RODRIGO ANUNCIAÇÃO CALDAS     MATRÍCULA: 619056124
#P2LEIMP: Diz qual é o maior número

nome = input("Olá! Por favor digite seu nome: ")                        #Pergunta o nome do usuário, guarda na variável "nome"
print("Bem-vindo(a)",nome,"!")                                          #Imprime o nome do usuário
a = int(input("Por favor, digite um número inteiro: "))                 #Pergunta um n° inteiro e guarda na variável "a"
b = int(input("Por favor, digite um novo número inteiro: "))            #Pergunta um n° inteiro e guarda na variável "b"
if  a > b:                                                              #Se a for maior que b
    print(a,"é maior do que",b,"!")                                     #O programa faz isso
elif a == b:                                                            #Se a e b forem iguais
    print("Eles são iguais!")                                           #O programa faz isso
else:                                                                   #Caso nenhuma das condições anteriores forem verdadeiras
    print(b,"é maior do que",a,"!")                                     #Ele faz isso