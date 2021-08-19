print("Bem vindo Professor")
print("P8MEDIAS.PY IMPRIME VARIOS ALUNOS SUA MATRICULA E SUAS DUAS NOTAS")
#DIÁLOGO DE ENTRADA DE DADOS
Smed = 0                      #inicialização do acumulador de medias
Nalunos = 0                   #inicialização do contador de alunos
MAXN = -1          #INICIALIZAÇÃO DA MAIOR NOTA: É A MENOR MAIOR NOTA POSSIVEL
MINN = 11          #INICIALIZAÇÃO DA MENOR NOTA: É A MAIOR MENOR NOTA POSSIVEL
Mat = int(input("Insira a matricula: "))
print(" Matricula informada: ",Mat)
while(Mat!=0):                         # encerramento
    Nota1 = float(input("Insira a nota: "))
    print("A nota inserida foi: ",Nota1)
    Nota2 = float(input("Insira a segunda nota: "))
    print("A nota inserida foi: ",Nota2)
#PROCESSAMENTO
    Med = (Nota1+Nota2)/2              # Media do aluno
    if Med < MINN:
        MINN = Med                    # NOVO MENOR
        Matmin = Mat
    if Med > MAXN:
        MAXN = Med                    # NOVO MAIOR
        Matmax = Mat
    if Med < 4:
        print(Mat," ",Nota1," ",Nota2," ",Med," Reprovado")
    else:
        if Med >= 6:
            print(Mat," ",Nota1," ",Nota2," ",Med," Aprovado")
        else:
            print(Mat," ",Nota1," ",Nota2," ",Med," VS")
    Smed = Smed + Med                 #acumula mais uma media
    Nalunos = Nalunos+1               #conta mais um aluno
    Mat = int(input("Insira a matricula: "))          # le uma...
    print("Matricula informada: ",Mat)                # ... nova matricula
#EMISSÃO DE RELATÓRIO DE SAÍDA
Medt = Smed / Nalunos                 #media da turma
print("\n A media da turma calculada: ",Medt)
print(" A maior media da turma: ",MAXN," Matricula: ",Matmax)
print(" A menor media da turma: ",MINN," Matricula: ",Matmin)
print(" Foram processados:",Nalunos,"alunos.")
#DESPEDIDA
print("\n Execução concluida")
#FINALIZAÇÃO
#