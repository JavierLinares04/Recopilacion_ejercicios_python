import random

respuesta = 0
respuesta_correcta = False
attempts = 0


def init_range():
    min = int (input("Introduce mínimo: "))
    max = int (input("Introduce máximo: "))
    global respuesta
    respuesta = random.randint(min,max)


def user_input():
    user_input = int (input("Introduce número: "))
    global attempts
    attempts+=1
    return user_input


init_range()
while not respuesta_correcta:
    uinput = user_input()
    if uinput == respuesta:
        print ("Respuesta correcta!")
        print ("El número de intentos ha sido: " + str(attempts))
        respuesta_correcta = True
        input()
        break

    else:
        if uinput < respuesta:
            print ("El número introducido es menor que el correcto")
        else:
            print ("El número introducido es mayor que el correcto")