"""
Declarar dos variables numericas
Obtener la suma la resta, la multiplicacion
Vamos a motrar las operaciones en 3 print utilizando f-string
"""
from tkinter import *

ventana = Tk()
ventana.title("calculadora")

e_texto = Entry(ventana, font=("Calibri 20"))
e_texto.grid(row=1,column=0,columnspan=4,padx=5,pady=5)

etiqueta = Label(ventana, text="Ingrese su usuario", font=("Calibri 20"))
etiqueta.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

ventana.mainloop()