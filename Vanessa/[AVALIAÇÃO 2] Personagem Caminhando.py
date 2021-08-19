# D	/ Personagem anda para a direita.
# E	/ Personagem anda para a esquerda.
# C / Personagem anda para cima.
# B	/ Personagem anda para baixo.

comando = input().strip()                      # casa 1
if comando == "D":
    comando = input().strip()                            # casa 2
    if comando == "C":
        print("X")
    elif comando == "E":
        print("V")
    elif comando == "B":
        print("P1")
    elif comando == "D":
        comando = input().strip()                                # casa 3
        if comando == "C":
            print("X")
        elif comando == "D":
            print("X")
        elif comando == "E":
            print("V")
        elif comando == "B":
            comando = input().strip()                             # casa 4
            if comando == "C":
                print("V")
            elif comando == "E":
                print("P1")
            elif comando == "D":
                print("P2")
            elif comando == "B":
                print("P3")
            else:
                print("I")
        else:
            print("I")
    else:
        print("I")
elif comando == "E":
    print("X")
elif comando == "C":
    print("X")
elif comando == "B":
    print("X")
else:
    print("I")
