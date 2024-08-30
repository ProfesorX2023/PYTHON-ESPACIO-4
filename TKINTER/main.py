import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk

#Crear la ventana principal
root = tk.Tk()
root.title("Ventana principal")

#Cargar la imagen
imagen = Image.open("fondo.png")
imagen = imagen.resize((800,600))
imagen_fondo = ImageTk.PhotoImage(imagen)

#crear un canvas
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill='both', expand=True)

#colocar la imagen en el canvas

canvas.create_image(0,0, image=imagen_fondo, anchor='nw')

# Colocar otros widgets en el canvas
label = tk.Label(root, text='Texto en la ventana', bg='white')
label_window = canvas.create_window(400,300,window=label)


root.mainloop()