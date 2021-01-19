continue_input = True
alumno_nombre = []
alumno_nota = []

while(continue_input):
    nombre = input("Introduzca nombre: ")
    nota = input("Introduzca nota: ")
    alumno_nombre.append(nombre)
    alumno_nota.append(nota)

    continue_answer = input("¿Continuar introduciendo datos? s/n\n")
    if continue_answer.lower() == 's':
        continue_input = True
    else:
        continue_input = False


nota_max = max(alumno_nota)
nota_min = min(alumno_nota)

indice_max = alumno_nota.index(nota_max)
indice_min = alumno_nota.index(nota_min)

alumno_max = [alumno_nombre[indice_max], alumno_nota[indice_max]]
alumno_min = [alumno_nombre[indice_min], alumno_nota[indice_min]]

with open('mediamaxmin.txt', 'w', encoding='utf8') as file:
    file.write("NOTA MAXIMA\n-----------------\n")
    file.write("Nombre: "+alumno_max[0]+"\nNota: "+alumno_max[1]+"\n")
    file.write("\n\n\n")
    file.write("NOTA MINIMA\n-----------------\n")
    file.write("Nombre: "+alumno_min[0]+"\nNota: "+alumno_min[1]+"\n")
    file.close()