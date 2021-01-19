import tkinter as tk
from tkinter import messagebox
import sys

saldo = 1000



#UI
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Cajero")
        self.geometry("250x250")

		#INGRESAR
        self.lbl_ing = tk.Label(text = "Ingresar (€):")
        self.lbl_ing.place(x=10,y=20)
        self.txtbx_ing=tk.Entry(self, width=12)
        self.txtbx_ing.place(x=80, y=20)
        self.btn_ingresar = tk.Button(self, text=u'\u2713' + "Confirmar",width=10, height=1, command=ingresar)
        self.btn_ingresar.place(x=160,y=17)

		#RETIRAR
        self.lbl_ret = tk.Label(text = "Retirar (€):")
        self.lbl_ret.place(x=10,y=80)
        self.txtbx_ret=tk.Entry(self, width=12)
        self.txtbx_ret.place(x=80, y=80)
        self.btn_retirar = tk.Button(self, text=u'\u2713' + "Confirmar",width=10, height=1, command=retirar)
        self.btn_retirar.place(x=160,y=77)

        #CONSULTAR
        self.btn_consultar = tk.Button(self, text="Consultar saldo",width=20, height=1, command=consultar)
        self.btn_consultar.place(x=50, y=140)

        #SALIR
        self.btn_salir = tk.Button(self, text="Salir",width=20, height=1, command=salir)
        self.btn_salir.place(x=50, y=200)



#FUNCIONES
def ingresar ():
    global saldo
    try:
        cantidad = int(gui.txtbx_ing.get())
        saldo += cantidad
        messagebox.showinfo(title="Ingreso", message="Se han ingresado: "+ str(cantidad) + "€")
    except:
        messagebox.showerror(title="Error", message="Valor inválido")


def retirar ():
    global saldo
    try:
        cantidad = int(gui.txtbx_ret.get())
        if cantidad > saldo:
            messagebox.showerror(title="Error", message="La cantidad sobrepasa el saldo disponible")
            return
        saldo -= cantidad
        messagebox.showinfo(title="Ingreso", message="Se han retirado: "+ str(cantidad) + "€")
    except:
        messagebox.showerror(title="Error", message="Valor inválido")


def consultar ():
    messagebox.showinfo(title="Saldo", message="El saldo actual de la cuenta es de: "+ str(saldo) + "€")


def salir ():
    sys.exit()




gui = GUI()
gui.resizable(False, False)
gui.mainloop()