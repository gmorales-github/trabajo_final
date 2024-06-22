import tkinter as tk
from tkinter import ttk
from services.crud import listar_productos
 
def main_menu():
    # Obtengo la lista de todos los productos
    productos = listar_productos()
    
    # Crear la ventana principal del menu
    window = tk.Tk()
    window.title("Menu principal")
    window.geometry("1225x600")
    window.resizable(width=False, height=False)
    window['bg'] = '#b0c6ff'


    # Cargo las columnas 
    columns = ("id_producto", "nombre_producto", "precio", "descripcion","stock", "id_marca")
    
    tv = ttk.Treeview(window, columns = columns, show="headings")
    tv.pack()

    tv.heading ('id_producto', text='id_producto', anchor=tk.CENTER)
    tv.heading ('nombre_producto', text="nombre_producto", anchor=tk.CENTER)
    tv.heading ('precio', text="precio", anchor=tk.CENTER)
    tv.heading ('descripcion', text='descripcion', anchor=tk.CENTER)
    tv.heading ('stock', text="stock", anchor=tk.CENTER)
    tv.heading ('id_marca', text="id_marca", anchor=tk.CENTER)
    
    tv.column  ('id_producto', anchor='e')
    tv.column  ('nombre_producto', anchor='e')
    tv.column  ('precio', anchor='e')
    tv.column  ('descripcion', anchor='e')
    tv.column  ('stock', anchor='e')
    tv.column  ('id_marca', anchor='e')

    # Recorro la lista de productos para insertar los valores dinámicamente en la tabla
    for producto in productos:
        tv.insert ('', tk.END, values = (producto))
    
    tv.grid (row=0, column=2, padx=10, pady=10)
    
    # Ejecutar la aplicación
    window.mainloop()