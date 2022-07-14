from cProfile import label
from tkinter import *

#definir la ventana y sus tamaños
ventana = Tk()
ventana.geometry("1000x500")
ventana.title("Alvamora")
ventana.resizable(0,0)
ventana.config(bg="red")
# Pantallas
def home():
    
    home_label.config(
        fg = "white",
        bg = "black",
        font = ("arial", 30),
        padx = 20,
        pady = 20

    )
    home_label.grid(row=8,column=0)

    #ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_removed()
    data_label.grid_removed()

    return True

def add():
    
    add_label.config(
        fg = "white",
        bg = "black",
        font = ("arial", 30),
        padx = 20,
        pady = 20

    )
    add_label.grid(row=8,column=0)
    return True

def info():
    
    info_label.config(
        fg = "white",
        bg = "black",
        font = ("arial", 30),
        padx = 20,
        pady = 20

    )
    info_label.grid(row=8,column=0)

    data_label = Label(ventana, text="jajant")
    data_label.grid(row=1,column=0)

    return True

#definir campos de pantalla
home_label = Label(ventana, text="Bienvenido")
add_label = Label(ventana, text="Agregar ventas")
info_label = Label(ventana, text="Informacion del vendedor o cosechador")

#crear menu

menu_superior = Menu(ventana)
menu_superior.add_command(label = "Inicio", command=home)
menu_superior.add_command(label = "Añadir", command=add)
menu_superior.add_command(label = "Información", command=info)
menu_superior.add_command(label = "Salir", command = ventana.quit)

#cargar menu
ventana.config(menu = menu_superior)





ventana.mainloop()