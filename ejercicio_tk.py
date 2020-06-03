from tkinter import *
import random

root = Tk()
root.resizable(width=0, height=0)
root.title("Tarea POO")

# Variables 

titulo = StringVar()
ruta = StringVar()
descripcion = StringVar()

# Etiquetas

# Proximamente un condicional (a ver vamos de nuevo!)

Label(root, text = "Ingrese sus datos", bg = "pink", fg = "white", width = 60, heigh = 1).grid(column=0, row=0, columnspan=3, sticky=W+E)
Label(root, text = "Titulo").grid(column = 0, row = 2, sticky = W)
Label(root, text = "Ruta").grid(column = 0, row = 3, sticky = W)
Label(root, text = "Descripcion").grid(column = 0, row = 4, sticky = W)

# Campos de entrada de datos

ent_titulo = Entry(root, textvariable = titulo)
ent_titulo.grid(column = 1, row = 2)
ent_titulo.focus_set()
ent_ruta = Entry(root, textvariable = ruta)
ent_ruta.grid(column = 1, row = 3)
ent_descripcion = Entry(root, textvariable = descripcion)
ent_descripcion.grid(column = 1, row = 4)

# Botones & Funciones

def imprimirConsola():
    print("Titulo: " + titulo.get() + "\n" + "Ruta: " + ruta.get() + "\n" + "Descripcion: " + descripcion.get())

alta = Button(root, padx = 25, text = "Alta", command = imprimirConsola)
alta.grid(column = 1, row = 6)

def cambioDeColor():
    colores = ["yellow", "green", "blue", "pink", "black", "orange", "red", "white", "grey", "violet"]
    root.config(bg = colores[random.randint(0, 9)])

sorpresa = Button(root, padx = 25, text = "Sorpresa", command = cambioDeColor)
sorpresa.grid(column = 2, row = 6)



mainloop()