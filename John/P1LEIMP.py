#P1LEIMP.PY
#UNIVERSIDADE FEDERAL FLUMINENSE
#ESCOLA DE ENGENHARIA
#ENG. REC. HÍDRICOS E DO MEIO AMBIENTE
#TCC00326 PROGRAMAÇÃO DE COMPUTADORES - TURMA B1
#SEMESTRE 2020.1
#PROF. JOHN REED
#DATA: 15/09/2020
#NOME: RODRIGO ANUNCIAÇÃO CALDAS     MATRÍCULA: 619056124
#P1LEIMP: Lê e imprime

nome = input("Olá! Por favor digite seu nome: ")      #Pergunta o nome do usuário, guarda na variável "nome"
print("Bem-vindo(a)",nome,"!")                        #Imprime o nome do usuário
idade = input("Diga a sua idade (em anos): ")         #Pergunta a idade do usário
idade = int(idade)                                    #Pega a variável "idade" transformando ela em numero inteiro e salvando na variável "idade"
if idade >= 18:                                           #Estrutura de condição, caso ela seja maior de 18
    print(nome,"tem",idade,"anos, portanto é maior de idade.") #Se for maior ou igual a 18 será impressa essa mensagem
else:
    print(nome,"tem",idade,"anos, portanto é menor de idade.") #caso seja menor de idade, será impressa essa mensagem
sexo = input("Escreva com qual sexo você se identifica (masculino ou feminino): ") #Pergunta o sexo
print(nome,"é do sexo",sexo,".")                              #Imprime o sexo do usuário
print(nome,"tem",idade,"anos de idade e pertence ao sexo",sexo,".")  #Imprime a ficha de cadastramento