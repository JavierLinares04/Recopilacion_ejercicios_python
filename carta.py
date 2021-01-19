import sqlite3

continue_input = True
input_data = []

while(continue_input):
    primer_plato = input("Introduzca primer plato: ")
    segundo_plato = input("Introduzca segundo plato: ")
    postre = input("Introduzca postre: ")
    platos = [primer_plato, segundo_plato, postre]
    input_data.append(platos)
    
    continue_answer = input("¿Continuar introduciendo datos? s/n\n")
    if continue_answer.lower() == 's':
        continue_input = True
    else:
        continue_input = False


conn = sqlite3.connect('carta.db')
c = conn.cursor()

c.execute('''CREATE TABLE carta
            (primer_plato text, segundo_plato text, postre text)''')

c.executemany('INSERT INTO carta VALUES(?,?,?);', input_data)

print('Creada base de datos con', c.rowcount*3, 'platos en la carta')

conn.commit()
conn.close()