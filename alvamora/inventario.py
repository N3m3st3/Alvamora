from cProfile import label
from tkinter import *
from turtle import left
import datetime
from tkinter import messagebox 

#definir la ventana y sus tamaños
ventana = Tk()
ventana.geometry("600x500")
ventana.title("Inventario")
ventana.resizable(0,0)
ventana.config(bg="red")
ventana.iconbitmap(r'C:\Users\Felipe\Desktop\avance gian\icono.ico')

encabezado = Label(ventana, text="Tenemos:") #titulo de la interfaz
encabezado.config(
    fg="white",
    bg="red",
    font=('', 15, 'bold'),
    padx=10,
    pady=10
)
# encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)
encabezado.grid(row=0, column=0,sticky=W)

tipo1 = Label(ventana, text="Total de paltas tipo 1:") #tipo de palta
tipo1.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
tipo1.grid(row=1, column=0,sticky=W)
# Checkbutton(ventana, text="Granel",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=1,column=1)
# Checkbutton(ventana, text="Por mayor",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=1,column=2)

tipo2 = Label(ventana, text="Total de paltas tipo 2:")
tipo2.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
tipo2.grid(row=2, column=0,sticky=W)
# Checkbutton(ventana, text="Tipo 1",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=2,column=1)
# Checkbutton(ventana, text="Tipo 2",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=2,column=2)
# Checkbutton(ventana, text="Tipo 3",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=2,column=3)
# Checkbutton(ventana, text="Tipo 4",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=2,column=4)

tipo3 = Label(ventana, text="Total de paltas tipo 3:")
tipo3.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
tipo3.grid(row=3, column=0,sticky=W)
# campo_texto = Entry(ventana)
# campo_texto.grid(row=3,column=1)

tipo4 = Label(ventana, text="Total de paltas tipo 4:")
tipo4.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
tipo4.grid(row=4, column=0,sticky=W)
# campo_texto = Entry(ventana)
# campo_texto.grid(row=4,column=1)

rutc = Label(ventana, text="Total de paltas:")
rutc.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
rutc.grid(row=5, column=0,sticky=W)
# campo_texto = Entry(ventana)
# campo_texto.grid(row=5,column=1)

preciov = Label(ventana, text="Total vendidas:")
preciov.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
preciov.grid(row=6, column=0,sticky=W)
# campo_texto = Entry(ventana)
# campo_texto.grid(row=6,column=1)




fecha = Label(vn, text=(f"{now.hour}:{now.minute}:{now.second}     {today.day}/ {today.month}/ {today.year}"),

boton = Button(ventana, text="Enviar")
boton.config(
    fg="white",
    bg="black",
    font=(20),
    padx=10,
    pady=5
)
boton.grid(row=8, column=1,sticky=NE)

ventana.mainloop()