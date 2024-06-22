import tkinter as tk
from tkinter import ttk
from services.crud import listar_productos
 
def main_menu():
    # Obtengo la lista de todos los productos
    productos = listar_productos()
    
    # Crear la ventana principal del menu
    window = tk.Tk()
    window.title("Gestión de productos")
    window.geometry("1225x600")
    window.resizable(width=False, height=False)
    window['bg'] = '#b0c6ff'


    # Cargo las columnas 
    columns = ("id_producto", "nombre_producto", "precio", "descripcion","stock", "id_marca")
    
    # Genero la tabla
    tv = ttk.Treeview(window, columns = columns, show="headings")
    tv.pack()

    # Recorro la lista de columnas para generar dinámicamente los encabezados
    for head in columns:
        tv.heading (head, text=head, anchor=tk.CENTER)

    # Recorro la lista de columnas para generar las columnas dinámicamente en la tabla
    for column in columns:
        tv.column  (column, anchor='e')
    
    # Recorro la lista de productos para insertar los valores dinámicamente en la tabla
    for producto in productos:
        tv.insert ('', tk.END, values = (producto))
    
    tv.grid (row=0, column=2, padx=10, pady=10)
    
    # Ejecutar la aplicación
    window.mainloop()