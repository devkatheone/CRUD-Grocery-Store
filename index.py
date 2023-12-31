from tkinter import ttk
from tkinter import *

import sqlite3 

#Aca definimos todo lo que tiene que ver con los productos
class Product:
    
    def __init__(self, window):
        self.wind = window 
        self.wind.title('Principal')
        
        #Frame Container
        frame = LabelFrame(self.wind, text = 'Agregar Producto')
        frame.grid (row = 0, column = 0, columnspan = 3, pady = 20)
        
        #Entrada de nombre de producto
        Label(frame, text = 'Nombre: ').grid(row = 1, column =0)
        self.name = Entry(frame)
        self.name.grid(row = 1, column = 1)

        #Entrada de precio del producto
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry (frame)
        self.price.grid(row = 2, column = 1)

        #Boton agregar producto
        ttk.Button(frame, text = 'Guardar Producto').grid(row = 3, columnspan = 2, sticky = W + E)




#Ventana principal
if __name__ == '__main__':
    window = Tk() 
    application = Product(window)
    window.mainloop()

