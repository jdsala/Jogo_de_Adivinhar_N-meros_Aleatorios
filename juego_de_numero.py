from ast import Break
import random


def jugar_numero():

    print("**************************************")
    print("Bien venido al juego de: ",  "ACIERTE EL NÚMERO!")
    print("**************************************")

    #Variaveis
    numero_secreto = random.randrange(1, 51)
    total_de_intentos = 0
    puntos = 1000

    print("Defina el nivel del juego: ")
    print("(1) Facil (2) Intermedio (3) Profesional")

    nivel = int(input("Defina su nivel de juego: "))

    if(nivel == 1):
        total_de_intentos = 15
    elif(nivel == 2):
        total_de_intentos = 10
    else:
        total_de_intentos == 5

    for intento in range(1, total_de_intentos + 1):

        #Função format é uma string de interpolação
        print("Intentos {} de {}".format(intento, total_de_intentos))
        digite = input("Digite el número secreto entre 1 y 50: ")
        print("Usted digito el número: ", digite)

    # Aqui convertemos uma string para int
        digite_int = int(digite)

        if(digite_int < 1 or digite_int > 50):
            print("Digite el número secreto entre 1 y 50: ")
            continue

        correcto = digite_int == numero_secreto
        mayor = digite_int > numero_secreto
        menor = digite_int < numero_secreto

        if (correcto):
            print("Usted acerto!!. Felicitaciones!.","Total de puntos {}".format(puntos))
            print("       ___________      ")
            print("      '._==_==_=_.'     ")
            print("      .-\\:      /-.    ")
            print("     | (|:.     |) |    ")
            print("      '-|:.     |-'     ")
            print("        \\::.    /      ")
            print("         '::. .'        ")
            print("           ) (          ")
            print("         _.' '._        ")
            print("        '-------'       ") 
            break
    # Caso acertar o número o programa para de rodar

        else:
            if(mayor):
                print("Usted erro! El número digitado es mayor al número secreto. ")

            elif(menor):
                print("Usted erro! El número digitado es menor al número secreto. ")

            ##pontos perdidos da rodada
            puntos_perdidos = abs(numero_secreto - digite_int)

            #subtraindo os pontos perdidos da pontuação total
            puntos = puntos - puntos_perdidos

    print("Fin del juego!!")
