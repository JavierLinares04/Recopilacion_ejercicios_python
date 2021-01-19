times = []
keep_going = True


def get_input():
    hours = int(input("Introduce horas: "))
    minutes = int(input("Introduce minutos: "))
    seconds = int(input("Introduce segundos: "))
    total_seconds = (hours*3600) + (minutes*60) + seconds
    times.append(total_seconds)


def calculate_total():
    total_seconds = 0
    for time in times:
        total_seconds += time
    hours = round(total_seconds/3600)
    minutes = round((total_seconds%3600)/60)
    seconds = round((total_seconds%3600)%60)

    print ("Tiempo total: " + str(hours) + " horas, " + str(minutes) + " minutos y " + str(seconds) + " segundos")
    input()



while keep_going:
    get_input()
    uinput = input("Desea continuar introduciendo? s/n \n")
    if uinput.lower() == 's':
        print ("Continuando...")
    elif uinput.lower() == 'n':
        keep_going = False
    else:
        print ("Respuesta inválida. Cancelando...")
        keep_going = False

calculate_total()