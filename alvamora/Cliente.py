from cProfile import label
from tkinter import *
from turtle import left
import datetime
from tkinter import messagebox 

#definir la ventana y sus tamaños
ventana = Tk()
ventana.geometry("600x500")
ventana.title("Cliente")
ventana.resizable(0,0)
ventana.config(bg="red")
ventana.iconbitmap(r'C:\Users\Felipe\Desktop\avance gian\icono.ico')

encabezado = Label(ventana, text="Ingresar todos los datos")
encabezado.config(
    fg="white",
    bg="red",
    font=('', 15, 'bold'),
    padx=10,
    pady=10
    
)
# encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)
encabezado.grid(row=0, column=0,sticky=W)



tipopalta = Label(ventana, text="Tipo de cliente:")
tipopalta.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
tipopalta.grid(row=2, column=0,sticky=W)
Checkbutton(ventana, text="Granel",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=2,column=1)
Checkbutton(ventana, text="Mayorista",fg="white",bg="red",font=20,padx=10,pady=10).grid(row=2,column=2)



cantidad = Label(ventana, text="Ingrese nombre del cliente:")
cantidad.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
cantidad.grid(row=3, column=0,sticky=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=3,column=1)

rutv = Label(ventana, text="Rut del cliente:")
rutv.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
rutv.grid(row=4, column=0,sticky=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=4,column=1)

rutc = Label(ventana, text="dirección cliente:")
rutc.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
rutc.grid(row=5, column=0,sticky=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=5,column=1)

preciov = Label(ventana, text="Telefono del cliente:")
preciov.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
preciov.grid(row=6, column=0,sticky=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=6,column=1)

fecha = Label(ventana, text="Fecha:")
fecha.config(
    fg="white",
    bg="red",
    font=(20),
    padx=10,
    pady=10
)
fecha.grid(row=7, column=0,sticky=W)
campo_texto = Entry(ventana)
campo_texto.grid(row=7,column=1)

# def getfecha():                                   intento de colocar la fecha
#     resultado.set(fechainsta.get())

# fechainsta = datetime.datetime.now()
# resultado =StringVar()
# fecha = Label(ventana, textvariable=resultado)
# fecha.config(
#     fg="black",
#     bg="black",
#     font=(20),
#     padx=10,
#     pady=10
# )
# fecha.grid(row=4, column=1,sticky=W)

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