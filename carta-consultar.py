from tkinter import *
import sqlite3

conn = sqlite3.connect('carta.db')
c = conn.cursor()

c.execute('''SELECT * FROM carta;''')

rows = c.fetchall()

carta = [['Primer plato', 'Segundo plato', 'Postre']]
for row in rows:
    carta.append(row)
			 		
conn.commit()
conn.close()


class Table: 
    def __init__(self,root):
        for i in range(total_rows): 
            for j in range(total_columns):
                if i == 0:
                    self.e = Entry(root, width=20, font=('Arial',16,'bold'))
                else:
                    self.e = Entry(root, width=27, font=('Arial',12)) 
                self.e.grid(row=i, column=j) 
                self.e.insert(END, carta[i][j])

total_rows = len(carta)
total_columns = len(carta[0]) 
   

root = Tk() 
t = Table(root)
root.title("Carta")
root.mainloop() 